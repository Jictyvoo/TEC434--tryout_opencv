import cv2 as cv
import numpy as np
from providers.image_repository_provider import ImageRepositoryProvider
from utils.cv_helpers import fill_holes
from utils.generators import output_filename


class ObjectIdentifier(ImageRepositoryProvider):
    def export_image(self, input_name: str, output_folder: str, image) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(input_name) + ".png",
            image,
        )

    def segmentate(self, image: cv.Mat):
        # Start to apply the threshold
        normalized_image = cv.normalize(image, None, 0, 255, cv.NORM_MINMAX)
        image_with_blur = cv.GaussianBlur(normalized_image, (7, 7), 0, 0)
        image_threshold = cv.adaptiveThreshold(
            image_with_blur,
            255,
            cv.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv.THRESH_BINARY_INV,
            15,
            3,
        )
        morphology_image = cv.morphologyEx(
            image_threshold,
            cv.MORPH_CLOSE,
            cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11)),
        )

        image_result = fill_holes(morphology_image)
        return image_result

    def execute(self, filename: str, output_path: str):
        loaded_image = self._image_loader.load(filename, True)

        image_result = self.segmentate(loaded_image)

        self.export_image(filename, output_path, image_result)
        return image_result
