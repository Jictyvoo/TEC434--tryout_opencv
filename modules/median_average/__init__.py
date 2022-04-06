from typing import Final

import click
from modules.median_average.average_method import AverageNoiseRemover
from modules.median_average.median_method import MedianNoiseRemover

AVERAGE: Final = "average"
MEDIAN: Final = "median"


@click.command()
@click.option(
    "--output", default="./output/", help="The output directory for processed image"
)
@click.option(
    "--method",
    default=AVERAGE,
    help="The method used to process the images",
    show_default=True,
)
@click.argument("input-folder")
def remove_noise(input_folder: str, output: str, method: str):
    """
    A script that remove the noise from a image using all images in a giving folder.
    By default, the `avg` is used, to enable the median, please use the flag '--method'
    """
    if method == AVERAGE:
        noise_remover = AverageNoiseRemover()
        noise_remover.execute(input_folder, output)
    elif method == MEDIAN:
        noise_remover = MedianNoiseRemover()
        noise_remover.execute(input_folder, output)
    else:
        raise click.BadOptionUsage(
            option_name="--method",
            message="Only the options %s can be used" % str((AVERAGE, MEDIAN)),
        )
