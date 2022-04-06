import hashlib
from abc import ABC, abstractmethod
from datetime import datetime

import numpy as np
from providers.image_repository_provider import ImageRepositoryProvider


class NoiseRemover(ABC, ImageRepositoryProvider):
    def __init__(self) -> None:
        super().__init__()

    def export_image(self, output_folder: str, image) -> None:
        timestamp = str(datetime.now())
        filename = hashlib.md5(timestamp.encode())

        self._image_exporter.save(output_folder, filename.hexdigest() + ".png", image)

    @abstractmethod
    def _calculate_image(self, shape: tuple, all_images: tuple) -> tuple:
        pass

    def execute(self, input_folder: str, output_folder: str) -> None:

        # Getting all images from the giving path
        all_images = self._image_loader.load_all(path=input_folder)

        # Only execute if has at least 2 images
        if len(all_images) > 1:
            image_shape = all_images[0].shape

            result_image = np.array(
                self._calculate_image(image_shape, all_images), np.uint8
            )

            # Write the image to output
            self.export_image(output_folder, result_image)
