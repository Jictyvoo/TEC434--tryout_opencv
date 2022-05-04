import cv2 as cv
from modules.ground_truth.result import GtResult


class ImageInvertPair:
    def __init__(self, image) -> None:
        self._image = image
        self._inverted = ~image

    @property
    def image(self):
        return self._image

    @property
    def inverted(self):
        return self._inverted


class GtCalculator:
    def __init__(self, result, ground) -> None:
        self._result_image = result
        self._ground_image = ground

    def calculate(self) -> GtResult:
        result = GtResult()
        image_pair = ImageInvertPair(self._result_image)
        ground_pair = ImageInvertPair(self._ground_image)

        non_zero_ground = cv.countNonZero(ground_pair.image)
        non_zero_inverted_ground = cv.countNonZero(ground_pair.inverted)

        # true positive
        image_tp = cv.bitwise_and(ground_pair.image, image_pair.image)
        # false negative
        image_fn = cv.bitwise_and(ground_pair.image, image_pair.inverted)

        result.positive = (
            cv.countNonZero(image_tp) * 100 / non_zero_ground,
            cv.countNonZero(image_fn) * 100 / non_zero_ground,
        )

        # true negative
        image_tn = cv.bitwise_and(ground_pair.inverted, image_pair.inverted)
        # false positive
        image_fp = cv.bitwise_and(ground_pair.inverted, image_pair.image)

        result.negative = (
            cv.countNonZero(image_tn) * 100 / non_zero_inverted_ground,
            cv.countNonZero(image_fp) * 100 / non_zero_inverted_ground,
        )

        return result
