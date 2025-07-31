import pytest

from game import Game


@pytest.fixture
def game():
    return Game


def test_exeption_when_input_is_none(game):
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)


def test_exeption_when_input_len_unmatched(game):
    game = Game()
    with pytest.raises(TypeError):
        game.guess("12")
