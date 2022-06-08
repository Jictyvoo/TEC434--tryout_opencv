import cv2
import numpy as np
from modules.color_segmentation.hsv_colors import HSVColor
from providers.image_repository_provider import ImageRepositoryProvider
from utils.cv_helpers import fill_holes
from utils.generators import output_filename


class IdentifyColor(ImageRepositoryProvider):
    def export_image(self, input_name: str, output_folder: str, image) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(input_name) + ".png",
            image,
        )

    def segmentate(self, image: cv2.Mat, color_range: HSVColor) -> cv2.Mat:
        frame_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # show only the color in the range
        lower_color = np.array(color_range.min)
        upper_color = np.array(color_range.max)
        mask = cv2.inRange(frame_hsv, lower_color, upper_color)

        # show the result
        result = cv2.bitwise_and(image, image, mask=fill_holes(mask))

        return result

    def execute(self, filename: str, color_range: HSVColor, output_folder: str) -> None:
        image = self._image_loader.load(filename)
        result = self.segmentate(image, color_range)

        self.export_image(
            input_name=filename, output_folder=output_folder, image=result
        )
