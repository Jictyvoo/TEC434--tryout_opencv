import typing
from os.path import join
from pathlib import Path

import cv2


class ImageExporterRepository:
    def save(self, path: str, filename: str, content: typing.Any):
        Path(path).mkdir(parents=True, exist_ok=True)
        filepath = join(path, filename)
        print("Saving file to %s" % filepath)
        cv2.imwrite(
            filepath,
            content,
        )
