from layout.layout import Layout


class LayoutSet(object):

    def __init__(self, layouts=None):
        if layouts is None:
            layouts = []
        self.layouts = layouts

    def get_layout(self, image_size) -> Layout:
        pass