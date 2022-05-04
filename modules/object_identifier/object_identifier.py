import hashlib

from providers.image_repository_provider import ImageRepositoryProvider


class ObjectIdentifier(ImageRepositoryProvider):
    def export_image(self, inputname: str, output_folder: str, image) -> None:
        hash_filename = hashlib.md5(inputname.encode("utf-8")).hexdigest()
        index = inputname.rindex("/")
        filename = inputname[index + 1 :]

        self._image_exporter.save(
            output_folder,
            filename + hash_filename[: int(len(hash_filename) / 2)] + ".png",
            image,
        )

    def execute(self, filename: str, output_path: str):
        return self._image_loader.load(filename)
