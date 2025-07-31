from gameresult import GameResult


class Game:

    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("이거못읽으세여")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number: str) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        return GameResult(False, 0, 0)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 이네여?")
        if len(guess_number) != 3:
            raise TypeError("입력이 3자리가 아니네여?")
        if not guess_number.isdigit():
            raise TypeError("입력이 숫자가 아니에여?")
        if self._is_duplicate_number(guess_number):
            raise TypeError("입력이 중복 숫자가 있네여")

    def _is_duplicate_number(self, guess_number: str):
        return len(set(guess_number)) != 3
