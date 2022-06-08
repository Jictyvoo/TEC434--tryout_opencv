from enum import Enum

from modules.color_segmentation.intensity_range import IntensityRange


class HSVColor:
    def __init__(self, h: tuple, s: tuple = (0, 0), v: tuple = (0, 0)):
        self.h = IntensityRange(min=min(h), max=max(h))
        self.s = IntensityRange(min=min(s), max=max(s))
        self.v = IntensityRange(min=min(v), max=max(v))

    @property
    def min(self) -> tuple:
        return (self.h.min, self.s.min, self.v.min)

    @property
    def max(self) -> tuple:
        return (self.h.max, self.s.max, self.v.max)

    def __str__(self):
        return f"HSVColor(h={self.h}, s={self.s}, v={self.v})"

    def __repr__(self):
        return self.__str__()


class HSVColors(Enum):
    RED = HSVColor(h=(0, 29), s=(0, 255), v=(0, 255))
    YELLOW = HSVColor(h=(30, 59), s=(69, 147), v=(189, 221))
    LIGHT_YELLOW = HSVColor(h=(17, 32), s=(69, 189), v=(147, 221))
    GREEN = HSVColor(h=(60, 89), s=(25, 255), v=(55, 255))
    CYAN = HSVColor(h=(90, 119), s=(0, 255), v=(0, 255))
    BLUE = HSVColor(h=(120, 149), s=(0, 255), v=(0, 255))
    MAGENTA = HSVColor(h=(150, 179), s=(0, 255), v=(0, 255))

    def get(name: str):
        match name.upper():
            case "RED":
                return HSVColors.RED
            case "YELLOW":
                return HSVColors.YELLOW
            case "LIGHT_YELLOW":
                return HSVColors.LIGHT_YELLOW
            case "GREEN":
                return HSVColors.GREEN
            case "CYAN":
                return HSVColors.CYAN
            case "BLUE":
                return HSVColors.BLUE
            case "MAGENTA":
                return HSVColors.MAGENTA
        return None
