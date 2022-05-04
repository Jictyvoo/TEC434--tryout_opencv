from modules import ground_truth
from modules.ground_truth.gt_calculator import GtCalculator
from providers.image_repository_provider import ImageRepositoryProvider


class GroundTruth(ImageRepositoryProvider):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, input_filename: str, gt_filename: str) -> None:
        # Getting image from the giving path
        input_image = self._image_loader.load(path=input_filename, as_bw=True)
        gt_image = self._image_loader.load(path=gt_filename, as_bw=True)

        calculator = GtCalculator(input_image, gt_image)
        result = calculator.calculate()

        print("----------------------------")
        print("Verdadeiro Positivo: %.2f\nFalso Negativo: %.2f" % result.positive)
        print("Verdadeiro Negativo: %.2f\nFalso Positivo: %.2f" % result.negative)
