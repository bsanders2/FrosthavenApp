from MonsterNames import importClasses
names_classes = importClasses()

from Game import Game

def test_Monster_Stats():
    for level in range(8):
        _, classes = names_classes.keys(), names_classes.values()
        for cls in classes:
            cls(level, elite=0)
            cls(level, elite=1)