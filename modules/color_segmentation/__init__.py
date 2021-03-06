import click
from models.hsv_colors import HSVColor, HSVColors
from models.intensity_range import IntensityRange
from modules.color_segmentation.identify_color import IdentifyColor


def parseColorRange(color_range: str, light_color: bool) -> IntensityRange:
    target_color: HSVColor = HSVColors.RED.value
    colors = color_range.split("-", 1)
    if len(colors) == 2:
        if colors[0].isnumeric() and colors[1].isnumeric():
            target_color = IntensityRange(min=int(colors[0]), max=int(colors[1]))
        elif colors[0].isnumeric():
            value = int(colors[0])
            target_color = IntensityRange(
                min=min(target_color.min, value), max=max(target_color.max, value)
            )
        elif colors[1].isnumeric():
            value = int(colors[1])
            target_color = IntensityRange(
                min=min(target_color.min, value), max=max(target_color.max, value)
            )
    else:
        # search for the color by its name
        if color_range.isnumeric():
            target_color = HSVColor(
                h=(int(color_range), int(color_range)), s=(0, 0), v=(0, 0)
            )
        else:
            found_color = HSVColors.get(name=color_range)
            if found_color is not None:
                target_color = found_color.value
            if light_color:
                target_color = HSVColor(
                    h=(target_color.h.min - 23, target_color.h.max),
                    s=(target_color.s.min, target_color.s.max),
                    v=(target_color.v.min, target_color.v.max),
                )
    return target_color


@click.command()
@click.option(
    "--color-range",
    default="green",
    help="The color range that will be recognized by the algorithm",
)
@click.option(
    "--output", default="./output/", help="The output directory for processed image"
)
@click.option("--light-color", default=False, help="Enable the use of light color")
@click.argument("filename")
def color_segment(color_range: str, output: str, light_color: bool, filename: str):
    """
    A script that takes an image and segment it by color.
    """

    target_color = parseColorRange(color_range, light_color)
    algorithm = IdentifyColor()
    algorithm.execute(filename=filename, color_range=target_color, output_folder=output)
