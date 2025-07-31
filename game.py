class Game:
    def guess(self, guessNumber:str):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()

        if not guessNumber.isdigit():
            raise TypeError()
