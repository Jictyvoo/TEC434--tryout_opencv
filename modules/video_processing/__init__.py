import click
from modules.color_segmentation import parseColorRange
from modules.color_segmentation.identify_color import IdentifyColor
from modules.element_contours.biggest_calculator import BiggestElementCalculator
from modules.element_contours.element_extractor import ElementContourExtractor
from modules.video_processing.video_processor import VideoProcessor


@click.command()
@click.option(
    "--color-range",
    default="green",
    help="The color range that will be recognized by the algorithm",
)
@click.option(
    "--output", default="./output/", help="The output directory for processed image"
)
@click.argument("filename")
def video_processor(color_range: str, output: str, filename: str):
    """
    Open a video and extract the biggest element in it sorted by color
    """

    target_color = parseColorRange(color_range, False)
    color_threshold = IdentifyColor()
    algorithm = BiggestElementCalculator(
        threshold_func=lambda image: color_threshold.segmentate(
            image=image, color_range=target_color
        ),
        isModeTree=False,
    )

    extractor = VideoProcessor(
        frame_processor=lambda image_obj: (
            algorithm.execute(image=image_obj, is_sorted=True)
        )[1]
    )
    extractor.execute(filename, output_folder=output, debug_mode=True)
