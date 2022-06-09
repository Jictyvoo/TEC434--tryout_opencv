class IntensityRange:
    def __init__(self, max: int, min: int) -> None:
        self._max = max
        self._min = min

    @property
    def max(self) -> int:
        return self._max

    @property
    def min(self) -> int:
        return self._min
