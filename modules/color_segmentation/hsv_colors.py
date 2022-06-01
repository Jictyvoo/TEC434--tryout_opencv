from enum import Enum

from modules.color_segmentation.intensity_range import IntensityRange


class HSVColors(Enum):
    Red = IntensityRange(min=0, max=29)
    Yellow = IntensityRange(min=30, max=59)
    Green = IntensityRange(min=60, max=89)
    Cyan = IntensityRange(min=90, max=119)
    Blue = IntensityRange(min=120, max=149)
    Magenta = IntensityRange(min=150, max=179)

    def get(name: str):
        match name.upper():
            case "RED":
                return HSVColors.Red
            case "YELLOW":
                return HSVColors.Yellow
            case "GREEN":
                return HSVColors.Green
            case "CYAN":
                return HSVColors.Cyan
            case "BLUE":
                return HSVColors.Blue
            case "MAGENTA":
                return HSVColors.Magenta
        return None
