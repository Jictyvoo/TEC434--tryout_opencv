from typing import Any, Callable

import cv2
from modules.element_contours.contours import Contours
from providers.image_repository_provider import ImageRepositoryProvider
from utils.generators import output_filename


class ElementContourExtractor(ImageRepositoryProvider):
    def __init__(self, contour_finder: Callable[[Any], Contours]) -> None:
        self.__contour_finder = contour_finder
        super().__init__()

    def export_image(self, filename: str, output_folder: str, image: cv2.Mat) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(filename) + ".png",
            image,
        )

    def __draw_contours(self, image: cv2.Mat, contours: Contours) -> cv2.Mat:
        # Extract image in given contours
        contours_image = cv2.drawContours(image, [contours.biggest], 0, (0, 255, 0), 3)
        return contours_image

    def execute(self, filename: str, output_folder: str) -> None:
        image = self._image_loader.load(filename)

        contours = self.__contour_finder(image)
        processedImage = self.__draw_contours(image, contours)
        self.export_image(filename, output_folder, processedImage)
