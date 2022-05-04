from providers.image_repository_provider import ImageRepositoryProvider


class ObjectIdentifier(ImageRepositoryProvider):
    def execute(self, filename: str, output_path: str):
        return self._image_loader.load(filename)
