import requests
import pandas as pd

b = pd.read_csv("./neural_model/nsl-kdd/data.csv")

b["is_threat"] = "true"

data = b.iloc[0].to_dict()

for i in range(5):
    a = requests.post('http://localhost:8080/api/lstm/', data=data)

print("закончили")