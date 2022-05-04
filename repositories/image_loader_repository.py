import os
import typing
from os.path import isfile, join

import cv2


class ImageLoaderRepository:
    def load(self, path: str, as_bw=False) -> typing.Any:
        if as_bw:
            return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        return cv2.imread(path)

    def load_all(self, path: str, file_extension: str = ".png") -> tuple:
        images: list = []
        for file_name in os.listdir(path):
            filepath = join(path, file_name)
            if isfile(filepath):
                if file_name.endswith(file_extension):
                    images.append(cv2.imread(filepath))
            else:
                images.extend(self.load_all(filepath, file_extension=file_extension))

        return tuple(images)
