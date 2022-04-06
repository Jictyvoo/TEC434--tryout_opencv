import numpy as np
from modules.remove_noise.abstract_noise_remover import NoiseRemover


class AverageNoiseRemover(NoiseRemover):
    def __init__(self) -> None:
        super().__init__()

    def _calculate_image(self, shape: tuple, all_images: tuple) -> tuple:
        total_rows, total_columns, total_channels = shape
        result_image = np.zeros((total_rows, total_columns, total_channels), np.uint8)

        result_image = np.average(all_images, axis=0)
        return result_image
