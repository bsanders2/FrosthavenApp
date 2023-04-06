

from Game import Game


def test_Game_init():
    game = Game(1)
    for game in [Game(n) for n in range(10)]:
        assert(game)

