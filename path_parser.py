import base64
import os.path
import random

import requests
from tencent_cos_python.util import Util

from layout.layout_set import LayoutSet
from layout.preset.preset_names import preset_layout_set_names

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36']


def _download(image_url):
    resp = requests.get(image_url, headers={"User-Agent": random.choice(user_agent_list)})
    image_type = resp.headers["Content-Type"].split("/")[1]
    p = Util.get_random_path(non_dot_ext=image_type)
    with open(p, mode='wb') as f:
        f.write(resp.content)
    return p


def _parse_image(base64_json_array):
    image_json_array_str = base64.urlsafe_b64decode(str.encode(base64_json_array)).decode()
    image_json_array = eval(image_json_array_str)
    image_local_paths = []
    for image_url in image_json_array:
        p = _download(image_url)
        image_local_paths.append(p)
    return image_local_paths


def _parse_layout_set_config(base64_config):
    """
    TODO 自定义的LayoutSet
    :param base64_config:
    :return:
    """
    base64.decodebytes(str.encode(base64_config))
    return ""


def _parse_config(base64_config):
    config_json_str = base64.urlsafe_b64decode(str.encode(base64_config)).decode()
    return eval(config_json_str)


class PathParser(object):
    """
    路径解析器.
    路径格式 /montage/layout_set/${name}|base64(layoutSetConfigJson)/images/base64(imagesJsonArray)
    ${name}需要在preset_layout_set_names中
    """

    def __init__(self, path):
        self.path = path
        self.components = list(filter(lambda e: e != "" and e != "montage", self.path.split("/")))
        assert len(self.components) % 2 == 0, "路径格式错误"
        self.components_dict = {}
        for i in range(len(self.components) // 2):
            v = self.components[i * 2 + 1]
            v = v if not str.isnumeric(v) else float(v) if int(v) != float(v) else int(v)
            self.components_dict[self.components[i * 2]] = v

        for k in self.components_dict:
            if k == "layout_set":
                self.layout_set: LayoutSet = preset_layout_set_names[self.components_dict[k]]
                # self.layout_set = self._parse_layout_set_config(self.components_dict[k])
            elif k == "images":
                self.image_paths = _parse_image(self.components_dict[k])
            elif k == "config":
                self.config = _parse_config(self.components_dict[k])

        self.layout = self.layout_set.get_layout(len(self.image_paths))

    def clean_up(self):
        for i in self.image_paths:
            if os.path.exists(i):
                os.remove(i)
        self.layout.clean_up()
