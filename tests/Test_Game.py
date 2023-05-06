

from Game import Game, sortDraws
from MonsterNames import importClasses
monster_classes = importClasses()

def test_Game_init():
    for game in [Game(n) for n in range(8)]:
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

def test_Draw():
    game = Game(1)
    n1, n2 = game.drawCards() 
    assert n1 == n2 == None

    for mname, _ in monster_classes.items():
        game.addMonster(mname, elite=0)
    cards, _ = game.drawCards()
    assert len(cards) == len(monster_classes)
    for mname, _ in monster_classes.items():
        game.addMonster(mname, elite=1)
    assert len(cards) == len(monster_classes)

def test_Dont_Draw_For_Inactive_Monsters():
    game = Game(1)
    for name in monster_classes.keys():
        monster = game.addMonster(name)
        game.removeMonster(monster)
        ret1, ret2 = game.drawCards()
        assert ret1 == ret2 == None
        assert monster not in game.monsters

def test_displayOutput():
    game = Game(1)
    cards, monsters = None, None
    out = game.displayOutput(cards, monsters)
    assert out == "-"*50+'\n'+"-"*50+'\n'

    for mname in monster_classes.keys():
        game.addMonster(mname)
        cards, monsters = game.drawCards()
        cards, monsters = sortDraws(cards, monsters)
        game.displayOutput(cards, monsters)


def test_sortDraws():
    # By initiative and elite first

    pass