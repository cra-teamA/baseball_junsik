class Game:
    def _is_duplicate_number(self, guess_number: str):
        return len(set(guess_number)) != 3

    def guess(self, guessNumber: str):
        if guessNumber is None:
            raise TypeError("입력이 None 이네여?")
        if len(guessNumber) != 3:
            raise TypeError("입력이 3자리가 아니네여?")

        if not guessNumber.isdigit():
            raise TypeError("입력이 숫자가 아니에여?")

        if self._is_duplicate_number(guessNumber):
            raise TypeError("입력이 중복 숫자가 있네여")
?