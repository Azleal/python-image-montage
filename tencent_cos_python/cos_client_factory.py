import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

SPLITTER = "_"
PREFIX = SPLITTER.join(["montage", "cos", ""])


def get_cos_clients_from_env():
    cos_configs = {}
    cos_clients = {}
    for env in os.environ:
        if env.startswith(PREFIX):
            partial_key = env[len(PREFIX):]
            client_name, config_key = partial_key.split(SPLITTER)
            if client_name not in cos_configs:
                cos_configs[client_name] = {}
            cos_configs[client_name][config_key] = os.getenv(env)
    for client_name in cos_configs:
        assert "region" in cos_configs[client_name], "region必须存在"
        assert "secretid" in cos_configs[client_name], "secretid必须存在"
        assert "secretkey" in cos_configs[client_name], "secretkey必须存在"

        config_dict = cos_configs[client_name]
        token = config_dict["token"] if "token" in config_dict else None
        scheme = config_dict["scheme"] if "scheme" in config_dict else "https"

        config = CosConfig(Region=config_dict["region"], SecretId=config_dict["secretid"],
                           SecretKey=config_dict["secretkey"], Token=token, Scheme=scheme)

        bucket_name = cos_configs[client_name]["bucket"]
        cos_clients[bucket_name] = CosS3Client(config)

    return cos_clients


cos_clients = get_cos_clients_from_env()


class CosClientFactory(object):

    def __init__(self):
        pass

    @staticmethod
    def get(bucket_name) -> CosS3Client:
        assert bucket_name in cos_clients, "bucket:[%s]不存在" % bucket_name
        return cos_clients[bucket_name]
