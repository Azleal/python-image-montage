from enum import Enum


class FitEnum(Enum):
    Fill = "fill"
    Contain = "contain"
    Cover = "cover"
    NONE = "none"
    ScaleDown = "scale-down"

    def __init__(self, code):
        self.code = code
