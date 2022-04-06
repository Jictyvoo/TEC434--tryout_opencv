from repositories.image_loader_repository import ImageLoaderRepository
from repositories.image_saver_repository import ImageExporterRepository


class ImageRepositoryProvider:
    def __init__(self) -> None:
        self._image_exporter = ImageExporterRepository()
        self._image_loader = ImageLoaderRepository()
