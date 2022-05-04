from typing import Final

import click
from modules.ground_truth.ground_truth import GroundTruth
from modules.ground_truth.gt_calculator import GtCalculator
from modules.object_identifier.object_identifier import ObjectIdentifier
from repositories.image_loader_repository import ImageLoaderRepository


@click.command()
@click.option(
    "--output", default="./output/", help="The output directory for processed image"
)
@click.option("--gt", default="", help="The ground truth filename + path")
@click.argument("filename")
def segment_image(filename: str, output: str, gt: str):
    """
    A script that segmentates a image and then export it result.
    Optional: Define the output of the result
    Optional: Run the ground truth of the result image
    """
    identifier = ObjectIdentifier()
    result_image = identifier.execute(filename, output)
    if len(gt) > 0:
        gt_image = ImageLoaderRepository().load(path=gt, as_bw=True)

        calculator = GtCalculator(result_image, gt_image)
        result = calculator.calculate()
        print(str(result).replace("(::)", "\n"))
