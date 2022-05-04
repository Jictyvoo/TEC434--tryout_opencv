import hashlib

import cv2 as cv
import numpy as np
from providers.image_repository_provider import ImageRepositoryProvider


class ObjectIdentifier(ImageRepositoryProvider):
    def export_image(self, inputname: str, output_folder: str, image) -> None:
        hash_filename = hashlib.md5(inputname.encode("utf-8")).hexdigest()
        index = inputname.rindex("/")
        filename = inputname[index + 1 :].replace(".", "")

        self._image_exporter.save(
            output_folder,
            filename + "_" + hash_filename[: int(len(hash_filename) / 2)] + ".png",
            image,
        )

    def fillHoles(self, src):
        contours, hierarchy = cv.findContours(
            src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE
        )
        dst = np.zeros(src.shape, np.uint8)
        color = 255
        for i in range(len(contours)):
            cv.drawContours(dst, contours, i, color, -1, 8, hierarchy, 0)
        return dst

    def execute(self, filename: str, output_path: str):
        loaded_image = self._image_loader.load(filename, True)

        # Start to apply the threshold
        normalized_image = cv.normalize(loaded_image, None, 0, 255, cv.NORM_MINMAX)
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

        image_result = self.fillHoles(morphology_image)

        self.export_image(filename, output_path, image_result)
        return image_result
