from PIL import Image

from layout.config import IMAGE_MODE
from layout.fit_enum import FitEnum


class Cell(object):

    def __init__(self, width, height, offset_x=0, offset_y=0, padding=0, scale=1, fit=FitEnum.Cover):
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.padding = padding
        self.scale = scale
        self.fit = fit

    def get_cell_box(self):
        return int(self.offset_x * self.scale), int(self.offset_y * self.scale), \
               int((self.offset_x + self.width) * self.scale), int((self.offset_y + self.height)  * self.scale),

    def get_image_box(self):
        return int((self.offset_x + self.padding) * self.scale), int((self.offset_y + self.padding) * self.scale), \
               int((self.offset_x + self.width - self.padding) * self.scale), \
               int((self.offset_y + self.height - self.padding) * self.scale)

    def rescale(self, scale):
        self.scale = scale
        return self

    def get_cell_image(self, image_path):
        image = Image.open(image_path).convert(IMAGE_MODE)
        image_size = (self.get_image_box()[2] - self.get_image_box()[0],
                      self.get_image_box()[3] - self.get_image_box()[1],)

        image = image.resize(image_size)
        return self.get_image_box(), image
