from Game import Game, sortDraws
from GUI.GUI import play

def test_Add_Monster_When_Frames_Are_Full():
    pass

def test_Play_Turn_With_No_Monsters():
    game = Game(1)
    cards, monsters = game.drawCards()
    cards, monsters = sortDraws(cards, monsters)
    game.displayOutput(cards, monsters)

def test_play():
    pass
    # play()