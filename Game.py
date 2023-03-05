# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:31:42 2023

@author: blake
"""

from Monsters import *
from difflib import get_close_matches

class Game():
    def __init__(self, level):
        self.level = level
        self.monsters = set()
        self.active_monsters = set()
        self.decks = dict()
    
    def addMonster(self, name, elite=0):
        if name in globals():
            obj = globals()[name]
            monster = obj(self.level, elite)
            self.monsters.add(monster)
            self.decks[monster.name] = monster.buildDeck()
            self.active_monsters.add(monster.name)
        else:
            print("{} not in Monsters.py, found close match {}".format(name, get_close_matches(name, globals())))
			
    def removeMonster(self, name, elite=0):
        for m in self.monsters:
            if m.name==name and m.elite==elite:
                if len([m.name for m in self.monsters if m.name==name]) == 1:
                    # Last monster of that type, stop drawing for it
                    self.active_monsters.remove(m.name)
                self.monsters.remove(m)
                return

        print("{} not in self.monsters, found close match {}".format(name, get_close_matches(name, [x.name for x in self.monsters])))
			
            
    def draw(self):
        if len(self.active_monsters) == 0:
            return
        print("-"*50)
        cards = {name : self.decks[name].draw() for name in self.active_monsters}
        cards, monsters = zip(*sorted(zip([cards[m.name] for m in self.monsters],self.monsters), key = lambda x: [x[0].initiative,x[1].getName()]))
        for card, monster in zip(cards, monsters):
            print(monster.getName() + ': ' + card.name + ' : ' + str(card.initiative))
            print(monster.calcAction(card))
        print("-"*50)
            
if __name__ == '__main__':
    game = Game(1)
    game.addMonster("AlgoxArcher")
    game.addMonster("AlgoxArcher", elite=1)
    game.addMonster("AlgoxGuard", elite=1)
    game.addMonster("AlgoxScout")
    game.addMonster("AlgoxScout", elite=1)
    game.draw()
    game.removeMonster("AlgoxArcher")
    game.draw()
    game.removeMonster("AlgoxArcher", elite=1)
    game.draw()
    game.removeMonster("AlgoxGuard", elite=1)
    game.draw()
    game.removeMonster("AlgoxScout")
    game.draw()
    game.removeMonster("AlgoxScout", elite=1)
    game.draw()