import click
import cv2
from modules.color_segmentation import parseColorRange
from modules.color_segmentation.identify_color import IdentifyColor
from modules.element_contours.bigsmal_calculator import BigSmallElementCalculator
from modules.video_processing.video_processor import VideoProcessor
from utils.cv_helpers import draw_contours


def frame_contour_processor(
    algorithm: BigSmallElementCalculator, image_obj: cv2.Mat
) -> cv2.Mat:
    contours, frame = algorithm.execute(image=image_obj, is_sorted=True)
    return draw_contours(frame, contours)


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
    Open a video and generate a new one, showing the biggest element in it sorted by color
    """

    target_color = parseColorRange(color_range, False)
    color_threshold = IdentifyColor()

    extractor = VideoProcessor(
        frame_processor=lambda image_obj: frame_contour_processor(
            image_obj=image_obj,
            algorithm=BigSmallElementCalculator(
                threshold_func=lambda image: color_threshold.segmentate(
                    image=image, color_range=target_color
                ),
                isModeTree=False,
            ),
        )
    )
    extractor.execute(filename, output_folder=output, debug_mode=True)
