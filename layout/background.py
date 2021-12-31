from PIL import Image, ImageColor

from layout.config import TRANSPARENT, IMAGE_MODE
from layout.fit_enum import FitEnum


class Background(object):
    """
    背景信息
    """

    def __init__(self, width, height, fit=FitEnum.Cover, transparent=1, color='white', scale=1):
        assert width > 0, "width error"
        assert height > 0, "height error"
        assert 1 >= transparent >= 0, "transparent error"
        self.width = width
        self.height = height
        self.fit = fit
        self.transparent = transparent
        self.color = color
        self.scale = scale

    def rescale(self, scale):
        self.scale = scale
        return self

    def get_image(self, image_url=None) -> Image:
        alpha = int(self.transparent * TRANSPARENT)
        rgb_color = ImageColor.getrgb(self.color)
        size = (int(self.width * self.scale), int(self.height * self.scale))
        # TODO 如果有图片地址的话需要显示图片地址

        return Image.new(IMAGE_MODE, size, rgb_color + (alpha, ))
