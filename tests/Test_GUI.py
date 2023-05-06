from Game import Game, sortDraws
from GUI.GUI import play

from GUI.GUI_Support import MonsterFrame, loadImage

from MonsterNames import importClasses
names_classes = importClasses()

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

def testLoadImage():
    names, classes = names_classes.keys(), names_classes.values()
    for name, cls in zip(names, classes):
        cls.elite=0
        cls.standee=1
        loadImage(cls)