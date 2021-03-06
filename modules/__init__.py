from typing import Final

from modules.color_segmentation import color_segment
from modules.element_contours import element_size
from modules.ground_truth import calculate_gt
from modules.morphology import morph_op
from modules.object_identifier import segment_image
from modules.remove_noise import remove_noise
from modules.video_processing import video_processor

"""A tuple that contains all cli functions for every module"""
MODULES_CLI: Final = [
    remove_noise,
    calculate_gt,
    segment_image,
    morph_op,
    color_segment,
    element_size,
    video_processor,
]
