from django.db import models


class LSTM_Neural_Model(models.Model):
    duration = models.CharField(max_length=255)
    protocol_type = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    src_bytes = models.CharField(max_length=255)
    dst_bytes = models.CharField(max_length=255)
    land = models.CharField(max_length=255)
    wrong_fragment = models.CharField(max_length=255)
    urgent = models.CharField(max_length=255)
    hot = models.CharField(max_length=255)
    num_failed_logins = models.CharField(max_length=255)
    logged_in = models.CharField(max_length=255)
    num_compromised = models.CharField(max_length=255)
    root_shell = models.CharField(max_length=255)
    su_attempted = models.CharField(max_length=255)
    num_root = models.CharField(max_length=255)
    num_file_creations = models.CharField(max_length=255)
    num_shells = models.CharField(max_length=255)
    num_access_files = models.CharField(max_length=255)
    num_outbound_cmds = models.CharField(max_length=255)
    is_host_login = models.CharField(max_length=255)
    is_guest_login = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    srv_count = models.CharField(max_length=255)
    serror_rate = models.CharField(max_length=255)
    srv_serror_rate = models.CharField(max_length=255)
    rerror_rate = models.CharField(max_length=255)
    srv_rerror_rate = models.CharField(max_length=255)
    same_srv_rate = models.CharField(max_length=255)
    diff_srv_rate = models.CharField(max_length=255)
    srv_diff_host_rate = models.CharField(max_length=255)
    dst_host_count = models.CharField(max_length=255)
    dst_host_srv_count = models.CharField(max_length=255)
    dst_host_same_srv_rate = models.CharField(max_length=255)
    dst_host_diff_srv_rate = models.CharField(max_length=255)
    dst_host_same_src_port_rate = models.CharField(max_length=255)
    dst_host_srv_diff_host_rate = models.CharField(max_length=255)
    dst_host_serror_rate = models.CharField(max_length=255)
    dst_host_srv_serror_rate = models.CharField(max_length=255)
    dst_host_rerror_rate = models.CharField(max_length=255)
    dst_host_srv_rerror_rate = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)

    class Meta:
        verbose_name = "LSTM"
        verbose_name_plural = "LSTM`s"

    def __str__(self) -> str:
        return f"LSTM(id={self.id})"