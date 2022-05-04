from modules.ground_truth.exception import GtResultException


class TrueFalse:
    def __init__(self, is_positive: bool, truth: float, fake: float) -> None:
        self.names = ("positive", "negative")
        if not is_positive:
            self.names = ("negative", "positive")
        self.truth = truth
        self.fake = fake

    def __repr__(self) -> str:
        return "`true %s`: %.2f; `false %s`: %.2f" % (
            self.names[0],
            self.truth,
            self.names[1],
            self.fake,
        )


class GtResult:
    def __init__(self) -> None:
        self._positive = TrueFalse(True, 0, 0)
        self._negative = TrueFalse(False, 0, 0)

    @property
    def positive(self) -> tuple:
        return (self._positive.truth, self._positive.fake)

    def __set_checker(self, truefake: tuple[float]) -> None:
        assert len(truefake) == 2, "Please only provide two args"
        value_sum = truefake[0] + truefake[1]
        between_0_1 = value_sum >= 0 and value_sum <= 1
        between_0_100_percent = value_sum >= 0 and value_sum <= 100
        if not (between_0_1 or between_0_100_percent):
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

    def __repr__(self) -> str:
        return "%s(::)%s" % (self._positive, self._negative)
