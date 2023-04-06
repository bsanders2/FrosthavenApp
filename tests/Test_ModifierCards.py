

# from src.Monsters import *
import MonsterNames as MonsterNames
from ModifierCards import ModifierCard, Deck, DeckFactory

def test_Deck():
    

    # init
    deck = Deck()
    # addCard
    for nm in range(8):
        deck.addCard(ModifierCard(nm,None,None,None))

    decks = [DeckFactory.buildDeck(name) for name in MonsterNames._MONSTER_NAMES_]
    ## draw
    for deck in decks:
        for _ in range(1000):
            deck.draw()



def test_DeckFactory():
    for name in MonsterNames._MONSTER_NAMES_:
        DeckFactory.buildDeck(name)

if __name__ == "__main__":
    test_Deck()