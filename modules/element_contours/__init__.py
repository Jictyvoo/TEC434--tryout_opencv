import click
from modules.color_segmentation import parseColorRange
from modules.color_segmentation.identify_color import IdentifyColor
from modules.element_contours.biggest_calculator import BiggestElementCalculator
from modules.element_contours.element_extractor import ElementContourExtractor


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
def biggest_element(color_range: str, output: str, light_color: bool, filename: str):
    """
    A script that takes an image and identify the biggest element by color.
    """

    target_color = parseColorRange(color_range, light_color)
    color_threshould = IdentifyColor()
    algorithm = BiggestElementCalculator(
        threshold_func=lambda image: color_threshould.segmentate(
            image=image, color_range=target_color
        ),
        isModeTree=False,
    )

    extractor = ElementContourExtractor(
        contour_finder=lambda image_obj: algorithm.execute(
            image=image_obj, is_sorted=True
        )
    )
    extractor.execute(filename, output_folder=output)
