import cv2 as cv
from modules.ground_truth.result import GtResult


class GtCalculator:
    def __init__(self, result, ground) -> None:
        self._result_image = result
        self._ground_image = ground

    def calculate(self) -> GtResult:
        result = GtResult()
        # true positive
        image_tp = cv.bitwise_and(self._ground_image, self._result_image)
        # false negative
        image_fn = cv.bitwise_and(self._ground_image, ~self._result_image)

        result.positive = (
            cv.countNonZero(image_tp) * 100 / cv.countNonZero(self._ground_image),
            cv.countNonZero(image_fn) * 100 / cv.countNonZero(self._ground_image),
        )

        # true negative
        image_tn = cv.bitwise_and(~self._ground_image, ~self._result_image)
        # false positive
        image_tp = cv.bitwise_and(~self._ground_image, self._result_image)

        result.negative = (
            cv.countNonZero(image_tn) * 100 / cv.countNonZero(~self._ground_image),
            cv.countNonZero(image_tp) * 100 / cv.countNonZero(~self._ground_image),
        )

        return result
