from typing import Callable, Union

import cv2
from modules.element_contours.contours import Contours


class BiggestElementCalculator:
    def __init__(
        self, threshold_func: Callable[[cv2.Mat], cv2.Mat], isModeTree: bool
    ) -> None:
        self.__threshold_func = threshold_func
        self.__mode = isModeTree and cv2.RETR_TREE or cv2.RETR_CCOMP

    def execute(self, image: str, is_sorted=False) -> Union[Contours, cv2.Mat]:
        # Convert the image to grayscale

        filtered_image = self.__threshold_func(image)
        gray_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(
            gray_image, self.__mode, cv2.CHAIN_APPROX_SIMPLE
        )
        if not is_sorted:
            return Contours(contours=contours, hierarchy=hierarchy, is_sorted=False)

        sortedContours = sorted(
            contours, key=lambda element: cv2.contourArea(element, False), reverse=True
        )
        return Contours(sortedContours, hierarchy, is_sorted=True), filtered_image
