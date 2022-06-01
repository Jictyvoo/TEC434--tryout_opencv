import cv2
import numpy as np
from modules.color_segmentation.intensity_range import IntensityRange
from providers.image_repository_provider import ImageRepositoryProvider
from utils.generators import output_filename


class IdentifyColor(ImageRepositoryProvider):
    def export_image(self, input_name: str, output_folder: str, image) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(input_name) + ".png",
            image,
        )

    def execute(
        self, filename: str, color_range: IntensityRange, output_folder: str
    ) -> None:
        image = self._image_loader.load(filename)
        frame_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # show only the color in the range
        lower_color = np.array([color_range.min, 25, 55])
        upper_color = np.array([color_range.max, 255, 255])
        mask = cv2.inRange(frame_hsv, lower_color, upper_color)

        # show the result
        result = cv2.bitwise_and(image, image, mask=mask)

        self.export_image(
            input_name=filename, output_folder=output_folder, image=result
        )
