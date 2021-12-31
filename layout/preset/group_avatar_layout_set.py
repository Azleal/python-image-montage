from layout.background import Background
from layout.cell import Cell
from layout.layout import Layout
from layout.layout_set import LayoutSet

IMAGE_SIZE_1 = 37, 37
IMAGE_SIZE_2 = 17, 17
IMAGE_SIZE_3 = 11, 11


class GroupAvatarLayoutSet(LayoutSet):
    """
    群组头像布局
    """

    def __init__(self):
        super().__init__()
        self.background = Background(IMAGE_SIZE_1[0], IMAGE_SIZE_1[1], color="#EEF2FB")
        self.layouts = [self._layout1(), self._layout2(), self._layout3(), self._layout4(),
                        self._layout5(), self._layout6(), self._layout7(), self._layout8(),
                        self._layout9()]

    def get_layout(self, image_size):
        assert image_size > 0, "图片数量应该大于0"
        image_size = image_size if image_size <= len(self.layouts) else len(self.layouts)
        return self.layouts[image_size - 1]

    def _layout1(self):
        cells = [Cell(*IMAGE_SIZE_1)]
        return Layout(self.background, cells)

    def _layout2(self):
        cells = [Cell(*IMAGE_SIZE_2, offset_x=1, offset_y=10),
                 Cell(*IMAGE_SIZE_2, offset_x=19, offset_y=10), ]
        return Layout(self.background, cells)

    def _layout3(self):
        cells = [Cell(*IMAGE_SIZE_2, offset_x=10, offset_y=1),
                 Cell(*IMAGE_SIZE_2, offset_x=1, offset_y=19),
                 Cell(*IMAGE_SIZE_2, offset_x=19, offset_y=19),
                 ]
        return Layout(self.background, cells)

    def _layout4(self):
        cells = [Cell(*IMAGE_SIZE_2, offset_x=1, offset_y=1),
                 Cell(*IMAGE_SIZE_2, offset_x=19, offset_y=1),
                 Cell(*IMAGE_SIZE_2, offset_x=1, offset_y=19),
                 Cell(*IMAGE_SIZE_2, offset_x=19, offset_y=19),
                 ]
        return Layout(self.background, cells)

    def _layout5(self):
        cells = [Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=7, offset_y=19),
                 Cell(*IMAGE_SIZE_3, offset_x=19, offset_y=19),
                 ]
        return Layout(self.background, cells)

    def _layout6(self):
        cells = [Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=7),
                 Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=19),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=19),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=19),
                 ]
        return Layout(self.background, cells)

    def _layout7(self):
        cells = [Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=25),
                 ]
        return Layout(self.background, cells)

    def _layout8(self):
        cells = [Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=7, offset_y=25),
                 Cell(*IMAGE_SIZE_3, offset_x=19, offset_y=25),
                 ]
        return Layout(self.background, cells)

    def _layout9(self):
        cells = [Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=1),
                 Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=13),
                 Cell(*IMAGE_SIZE_3, offset_x=1, offset_y=25),
                 Cell(*IMAGE_SIZE_3, offset_x=13, offset_y=25),
                 Cell(*IMAGE_SIZE_3, offset_x=25, offset_y=25),
                 ]
        return Layout(self.background, cells)
