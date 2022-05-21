import cv2
from providers.image_repository_provider import ImageRepositoryProvider
from utils.generators import output_filename


class ApplyStructuringElement(ImageRepositoryProvider):
    def __init__(self, execute_open_close: bool, is_rect_strel: bool) -> None:
        morph_element = is_rect_strel and cv2.MORPH_RECT or cv2.MORPH_CROSS

        self._strt_el = cv2.getStructuringElement(morph_element, (3, 3))
        self._execute_open_close = execute_open_close
        super().__init__()

    def export_image(self, input_name: str, output_folder: str, image) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(input_name) + ".png",
            image,
        )

    def execute(self, filename: str, output_folder: str) -> None:
        source_image = self._image_loader.load(filename, as_bw=True)
        image_erosion = cv2.morphologyEx(source_image, cv2.MORPH_ERODE, self._strt_el)
        image_dilation = cv2.morphologyEx(source_image, cv2.MORPH_DILATE, self._strt_el)

        self.export_image(filename + "_erosion", output_folder, image=image_erosion)
        self.export_image(filename + "_dilation", output_folder, image=image_dilation)

        if self._execute_open_close:
            image_open = cv2.morphologyEx(source_image, cv2.MORPH_OPEN, self._strt_el)
            image_close = cv2.morphologyEx(source_image, cv2.MORPH_CLOSE, self._strt_el)

            self.export_image(filename + "_open", output_folder, image=image_open)
            self.export_image(filename + "_close", output_folder, image=image_close)
