import hashlib
from datetime import datetime

import numpy as np
from providers.image_repository_provider import ImageRepositoryProvider


class AverageNoiseRemover(ImageRepositoryProvider):
    def __init__(self) -> None:
        super().__init__()

    def export_image(self, output_folder: str, image) -> None:
        timestamp = str(datetime.now())
        filename = hashlib.md5(timestamp.encode())

        self._image_exporter.save(output_folder, filename.hexdigest() + ".png", image)

    def execute(self, input_folder: str, output_folder: str) -> None:

        # Getting all images from the giving path
        all_images = self._image_loader.load_all(path=input_folder)

        # Only execute if has at least 2 images
        if len(all_images) > 1:
            total_rows, total_columns, total_channels = all_images[0].shape
            result_image = np.zeros(
                (total_rows, total_columns, total_channels), np.uint8
            )

            pixel_avg = np.average(all_images, axis=0)
            result_image = np.array(pixel_avg, np.uint8)

            # Write the image to output
            self.export_image(output_folder, result_image)
