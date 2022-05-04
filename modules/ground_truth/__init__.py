from typing import Final

import click
from modules.ground_truth.ground_truth import GroundTruth


@click.command()
@click.argument("base")
@click.argument("gt")
def calculate_gt(base: str, gt: str):
    """
    A script executes a ground truth calculation with two given images, a result and a to test.
    """
    gt_algorithm = GroundTruth()
    gt_algorithm.execute(base, gt)
