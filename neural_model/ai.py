import os
import requests
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
from keras.layers import Dense, LSTM, Dropout, Flatten
from keras.models import Sequential
from sklearn import preprocessing
from sklearn.preprocessing import LabelBinarizer


def create_path():
    current_file_path = os.path.abspath(__file__)
    current_directory = os.path.dirname(current_file_path)
    target_directory = os.path.abspath(os.path.join(current_directory, 'nsl-kdd'))
    for file_name in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file_name)
        if os.path.isfile(file_path):
            return file_path


class LSTMModelCreator:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def create_datas(self, data):
        train_data_90_percent = data.sample(frac=0.9)
        # service_data = data.drop(train_data_90_percent.index)
        # service_data.to_csv("../neural_model/nsl-kdd/data_for_service.csv")
        return train_data_90_percent

    def change_label(self, df):
        df["label"].replace(
            [
                "apache2",
                "back",
                "land",
                "neptune",
                "mailbomb",
                "pod",
                "processtable",
                "smurf",
                "teardrop",
                "udpstorm",
                "worm",
            ],
            "Dos",
            inplace=True,
        )
        df["label"].replace(
            [
                "ftp_write",
                "guess_passwd",
                "httptunnel",
                "imap",
                "multihop",
                "named",
                "phf",
                "sendmail",
                "snmpgetattack",
                "snmpguess",
                "spy",
                "warezclient",
                "warezmaster",
                "xlock",
                "xsnoop",
            ],
            "R2L",
            inplace=True,
        )
        df["label"].replace(
            ["ipsweep", "mscan", "nmap", "portsweep", "saint", "satan"],
            "Probe",
            inplace=True,
        )
        df["label"].replace(
            [
                "buffer_overflow",
                "loadmodule",
                "perl",
                "ps",
                "rootkit",
                "sqlattack",
                "xterm",
            ],
            "U2R",
            inplace=True,
        )
        df = df[df["label"] != "U2R"]
        return df

    def preprocess_data(self, data):
        data.drop(["difficulty"], axis=1, inplace=True)
        data = self.change_label(data)
        return data

    def change_float_to_int(self, df, cols):
        for col in cols:
            df[col] = df[col].apply(np.int8)
        return df

    def standardize(self, df, col):
        std_scaler = StandardScaler()
        for i in col:
            arr = df[i]
            arr = np.array(arr)
            df[i] = std_scaler.fit_transform(arr.reshape(len(arr), 1))
        return df

    def preprocess_train_data(self, data):
        label = pd.DataFrame(data["label"])
        numeric_col = data.select_dtypes(include="number").columns
        data = self.standardize(data, numeric_col)

        le2 = preprocessing.LabelEncoder()
        enc_label = label.apply(le2.fit_transform)
        data["intrusion"] = enc_label
        data.drop(labels=["label"], axis=1, inplace=True)
        data = pd.get_dummies(
            data, columns=["protocol_type", "service", "flag"], prefix="", prefix_sep=""
        )
        X_data = data.drop("intrusion", axis=1)
        y_data = data["intrusion"]
        # print("X_train has shape:", X_data.shape, "\ny_train has shape:", y_data.shape)
        y_data = LabelBinarizer().fit_transform(y_data)

        X_data = np.array(X_data)
        y_data = np.array(y_data)
        X_train, X_test, y_train, y_test = train_test_split(
            X_data, y_data, test_size=0.2, random_state=42
        )
        X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
        X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))
        return X_train, X_test, y_train, y_test

    def create_model(self):
        data = pd.read_csv(self.data_file_path).drop(columns=["Unnamed: 0"])
        data = self.create_datas(data)
        data = self.preprocess_data(data)
        X_train, X_test, y_train, y_test = self.preprocess_train_data(data)

        model = Sequential()
        model.add(
            LSTM(
                64,
                return_sequences=True,
                input_shape=(X_train.shape[1], X_train.shape[2]),
            )
        )
        model.add(Dropout(0.2))
        model.add(LSTM(64, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(32, return_sequences=True))
        model.add(Flatten())
        model.add(Dense(units=50))
        model.add(Dense(units=4, activation="softmax"))

        model.compile(
            loss="categorical_crossentropy",
            optimizer="adam",
            metrics=[
                "accuracy",
                tf.keras.metrics.Precision(),
                tf.keras.metrics.Recall(),
            ],
        )
        X_train = X_train.astype(float)
        y_train = y_train.astype(float)
        history = model.fit(
            X_train,
            y_train,
            epochs=30,
            batch_size=5000,
            validation_split=0.2,
            verbose=1,
        )
        X_test = X_test.astype(float)
        y_test = y_test.astype(float)
        test_results = model.evaluate(X_test, y_test, verbose=1)
        # print(
        #     f"Test results - Loss: {test_results[0]} - Accuracy: {test_results[1]*100}%"
        # )

        y_predict = model.predict(X_test)
        y_pred = np.argmax(y_predict, axis=-1)
        report = classification_report(np.argmax(y_test, axis=-1), y_pred)
        # print(report)

        return model, X_test


class TestModel:

    def __init__(self, data_file_path, model, csv_data):
        self.data_file_path = data_file_path
        self.model = model
        self.csv_data = csv_data

    def change_label(self, df):
        df["label"].replace(
            [
                "apache2",
                "back",
                "land",
                "neptune",
                "mailbomb",
                "pod",
                "processtable",
                "smurf",
                "teardrop",
                "udpstorm",
                "worm",
            ],
            "Dos",
            inplace=True,
        )
        df["label"].replace(
            [
                "ftp_write",
                "guess_passwd",
                "httptunnel",
                "imap",
                "multihop",
                "named",
                "phf",
                "sendmail",
                "snmpgetattack",
                "snmpguess",
                "spy",
                "warezclient",
                "warezmaster",
                "xlock",
                "xsnoop",
            ],
            "R2L",
            inplace=True,
        )
        df["label"].replace(
            ["ipsweep", "mscan", "nmap", "portsweep", "saint", "satan"],
            "Probe",
            inplace=True,
        )
        df["label"].replace(
            [
                "buffer_overflow",
                "loadmodule",
                "perl",
                "ps",
                "rootkit",
                "sqlattack",
                "xterm",
            ],
            "U2R",
            inplace=True,
        )
        df = df[df["label"] != "U2R"]
        return df

    def preprocess_data(self, data):
        data.drop(["difficulty"], axis=1, inplace=True)
        data = self.change_label(data)
        return data

    def change_float_to_int(self, df, cols):
        for col in cols:
            df[col] = df[col].apply(np.int8)
        return df

    def standardize(self, df, col):
        std_scaler = StandardScaler()
        for i in col:
            arr = df[i]
            arr = np.array(arr)
            df[i] = std_scaler.fit_transform(arr.reshape(len(arr), 1))
        return df

    def preprocess_train_data(self, data):
        label = pd.DataFrame(data["label"])
        numeric_col = data.select_dtypes(include="number").columns
        data = self.standardize(data, numeric_col)

        le2 = preprocessing.LabelEncoder()
        enc_label = label.apply(le2.fit_transform)
        data["intrusion"] = enc_label
        data.drop(labels=["label"], axis=1, inplace=True)
        data = pd.get_dummies(
            data, columns=["protocol_type", "service", "flag"], prefix="", prefix_sep=""
        )
        X_data = data.drop("intrusion", axis=1)
        y_data = data["intrusion"]
        # print("X_train has shape:", X_data.shape, "\ny_train has shape:", y_data.shape)
        y_data = LabelBinarizer().fit_transform(y_data)

        X_data = np.array(X_data)
        y_data = np.array(y_data)
        X_data = np.reshape(X_data, (X_data.shape[0], 1, X_data.shape[1]))
        return X_data

    def test_model(self, X_data):

        X_data = X_data[-1000:]
        self.csv_data["is_threat"] = "false"
        res = self.model.predict(X_data)

        return res, self.csv_data


class DataSetProcessor:
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def prepare_dataset_with_bool_params(self):
        for ind, params, in enumerate(self.input):
            self.check_params(ind, params)
        return self.output

    def check_params(self, index, param):
        print(type(param[0]), param[0], param)
        if param[0] > 0.7:
            self.output["is_threat"].iloc[index] = "true"
        else:

            self.output["is_threat"].iloc[index] = "false"


def run():
    data_file_path = create_path()  # "./nsl-kdd/data.csv"
    model_creator = LSTMModelCreator(data_file_path)

    model, X_test = model_creator.create_model()

    test_model = TestModel(
        create_path(),
        model, pd.read_csv(data_file_path)[-1000:])

    input, output = test_model.test_model(X_test)
    processor = DataSetProcessor(input, output)

    data_set_for_send = processor.prepare_dataset_with_bool_params()

    bad_traffic = data_set_for_send[data_set_for_send["is_threat"] == "true"]
    print(bad_traffic, "Подозрительный трафик, выявленный моделью")

    for index in range(len(data_set_for_send)):
        if index == 30:
            break
        data = data_set_for_send.iloc[index].to_dict()
        print(data)
        req = requests.post("http://localhost:8080/api/lstm/", data=data)
        print(req.status_code, req.json(), f"Наш {index} POST запрос")


if __name__ == "__main__":
    run()

