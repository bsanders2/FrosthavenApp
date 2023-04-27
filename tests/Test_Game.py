

from Game import Game
from MonsterNames import importClasses
monster_classes = importClasses()

def test_Game_init():
    game = Game(1)
    for game in [Game(n) for n in range(10)]:
        assert(game)

def test_Game_Add_And_Remove_Standees():
    game = Game(1)
    for _, mclass in monster_classes.items():
        added_so_far = set([])
        for i in range(1, mclass.num_standees+1):
            monster = game.addMonster(mclass.name) 
            added_so_far.add(monster.standee)
            assert len(added_so_far) == i # unique numbers assigned each time

    for _, mclass in monster_classes.items():
        added_so_far = set([])
        for i in range(1, mclass.num_standees+1):
            monster = mclass(1)
            monster.standee = i
            game.removeMonster(monster)
            active_standees = [x.standee for x in game.monsters if x.name==monster.name] 
            assert len(active_standees) == monster.num_standees - i     

def test_Add_Monster_When_Frames_Are_Full():
    pass

def test_Sort_Action_Outputs():
    # By initiative and elite first
    pass