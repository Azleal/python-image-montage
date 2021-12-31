import os

from PIL import Image
from tencent_cos_python.util import Util

from layout.background import Background


class Layout(object):

    def __init__(self, background: Background, cells):
        self.background = background
        self.cells = cells
        self.assembled_image_path = Util.get_random_path(non_dot_ext="png")

    def assemble(self, cell_images, background_image_url=None, scale=1) -> Image:

        background_image = self.background.rescale(scale).get_image(background_image_url)
        for i in range(len(self.cells)):
            c = self.cells[i].rescale(scale)
            cell_image_box, cell_image = c.get_cell_image(cell_images[i])
            background_image.paste(cell_image, cell_image_box, cell_image)
        background_image.save(self.assembled_image_path)
        return background_image

    def clean_up(self):
        if os.path.exists(self.assembled_image_path):
            os.remove(self.assembled_image_path)
