import cv2


class Contours:
    def __init__(self, contours: tuple, hierarchy: any, is_sorted: bool) -> None:
        self.contours = contours
        self.hiearchy = hierarchy
        self._is_sorted = is_sorted

    @property
    def biggest(self) -> tuple:
        if not self._is_sorted:
            self.contours = sorted(
                self.contours,
                key=lambda element: cv2.contourArea(element, False),
                reverse=True,
            )
        return self.contours[0]
