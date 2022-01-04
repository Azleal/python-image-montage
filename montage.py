import base64
import os.path

from tencent_cos_python.cos_client_factory import CosClientFactory
from tencent_cos_python.util import Util

from tencent_cos_python.cos_object import CosObject

from path_parser import PathParser
import hashlib


bucket = Util.get_random_str(8) if "montage_bucket" not in os.environ else os.getenv("montage_bucket")
group_avatar_cos_prefix = os.path.join('/', 'group_avatar')
image_type = 'png'
cos_client = CosClientFactory(env_prefix="montage_cos_", env_splitter="_").get(bucket)

def main_handler(event, context):
    path = event["path"]
    path_md5 = hashlib.md5(path.encode('utf-8')).hexdigest()
    pre_generated_file_path = path_md5 + '.' + image_type
    assembled_image_key = os.path.join(group_avatar_cos_prefix, pre_generated_file_path, )
    assembled_cos_object = CosObject(bucket, assembled_image_key)

    parser = None

    if assembled_cos_object.object_exists(cos_client):
        local_assembled_image_path = assembled_cos_object.get_object()
    else:
        parser = PathParser(path)
        layout_set = parser.layout_set
        image_paths = parser.image_paths
        layout = layout_set.get_layout(len(image_paths))
        layout.assemble(image_paths, scale=1 if 'scale' not in parser.components_dict else float(parser.components_dict['scale']))
        if CosObject(bucket, assembled_image_key).has_cos_client():
            CosObject(bucket, assembled_image_key).put_object(layout.assembled_image_path)
        local_assembled_image_path = layout.assembled_image_path

    with open(local_assembled_image_path, 'rb') as f:
        image_data = f.read()

    if parser is not None:
        parser.clean_up()

    return to_image_stream(image_data, assembled_image_key)


def to_cos_object(image_data):
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "image/png"},
        "body": image_data
    }


def to_image_stream(image_data, key=''):
    base64_image_data = base64.b64encode(image_data).decode()
    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png",
            "key": key
        },
        "body": base64_image_data
    }
