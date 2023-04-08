

from Game import Game


def test_Game_init():
    game = Game(1)
    for game in [Game(n) for n in range(10)]:
        assert(game)

def test_Add_Monster_When_Frames_Are_Full():
    pass

