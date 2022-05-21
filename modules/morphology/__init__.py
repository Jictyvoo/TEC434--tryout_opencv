from typing import Final

import click
from modules.morphology.apply_structuring_element import ApplyStructuringElement

STRUCEL_CROSS: Final = "cross"
STRUCEL_RECT: Final = "rect"


@click.command()
@click.option(
    "--output", default="./output/", help="The output directory for processed image"
)
@click.option("--struct_el", default=STRUCEL_CROSS, help="The structuring element")
@click.option(
    "--open_close", default="false", help="Enable the use of open and close algorithms"
)
@click.argument("filename")
def morph_op(filename: str, output: str, struct_el: str, open_close: str):
    """
    A script that takes an image and apply a structuring element in it.
    Optional: Structuring Element, if not passed, it will use a default
    Optional: Default output
    """

    if struct_el != STRUCEL_CROSS and struct_el != STRUCEL_RECT:
        raise click.BadOptionUsage(
            option_name="--method",
            message="Only the options %s can be used"
            % str((STRUCEL_CROSS, STRUCEL_RECT)),
        )

    execute_open_close = open_close != "false"
    executor = ApplyStructuringElement(
        execute_open_close=execute_open_close,
        is_rect_strel=struct_el == STRUCEL_RECT,
    )

    executor.execute(filename, output)
