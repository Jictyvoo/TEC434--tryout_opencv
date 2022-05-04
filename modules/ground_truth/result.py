from modules.ground_truth.exception import GtResultException


class TrueFalse:
    def __init__(self, name: str, truth: float, fake: float) -> None:
        self.name = name
        self.truth = truth
        self.fake = fake

    def __repr__(self) -> str:
        return "`true %s`: %.2f; `false %s`: %.2f" % (
            self.name,
            self.truth,
            self.name,
            self.fake,
        )


class GtResult:
    def __init__(self) -> None:
        self._positive = TrueFalse("positive", 0, 0)
        self._negative = TrueFalse("negative", 0, 0)

    @property
    def positive(self) -> tuple:
        return (self._positive.truth, self._positive.fake)

    def __set_checker(self, truefake: tuple[float]) -> None:
        assert len(truefake) == 2, "Please only provide two args"
        value_sum = truefake[0] + truefake[1]
        if value_sum != 1 or value_sum != 100:
            raise GtResultException(
                "The sum of positive and true and false values should be 100%%; Received: %.2f"
                % value_sum
            )

    @positive.setter
    def positive(self, truefake: tuple[float]) -> None:
        self.__set_checker(truefake)
        self._positive.truth = truefake[1]
        self._positive.fake = truefake[0]

    @property
    def negative(self) -> tuple:
        return (self._negative.truth, self._negative.fake)

    @negative.setter
    def negative(self, truefake: tuple[float]) -> None:
        self.__set_checker(truefake)
        self._negative.truth = truefake[1]
        self._negative.fake = truefake[0]
