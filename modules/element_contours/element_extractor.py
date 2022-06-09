from typing import Callable, Union

import cv2
from models.contours import Contours
from providers.image_repository_provider import ImageRepositoryProvider
from utils.cv_helpers import draw_contours
from utils.generators import output_filename


class ElementContourExtractor(ImageRepositoryProvider):
    def __init__(
        self, contour_finder: Callable[[cv2.Mat], Union[Contours, cv2.Mat]]
    ) -> None:
        self.__contour_finder = contour_finder
        super().__init__()

    def export_image(self, filename: str, output_folder: str, image: cv2.Mat) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(filename) + ".png",
            image,
        )

    def execute(
        self, filename: str, output_folder: str, is_small: bool = False
    ) -> None:
        image = self._image_loader.load(filename)

        contours, filtered_image = self.__contour_finder(image)
        processedImage = draw_contours(filtered_image, contours, is_small=is_small)
        self.export_image(filename, output_folder, processedImage)
