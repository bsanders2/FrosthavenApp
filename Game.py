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
    
    def addMonster(self, name, elite=0):
        if name in globals():
            obj = globals()[name]
            self.monsters.add(obj(self.level, elite))
        else:
            print("{} not in Monsters.py, found close match {}".format(name, get_close_matches(name, globals())))
			
    def removeMonster(self, name, elite=0):
        if name in globals():
            obj = globals()[name]
            for item in self.monsters:
                if isinstance(item, obj):
                    self.monsters.remove(item)
                    break
        else:
            print("{} not in Monsters.py, found close match {}".format(name, get_close_matches(name, globals())))
			
            
    def draw(self):
        print("-"*50)
        cards = [m.draw() for m in self.monsters]
        cards, monsters = zip(*sorted(zip(cards,[x for x in self.monsters]), key = lambda x: x[0].initiative))
        for card, monster in zip(cards, monsters):
            print(monster.name + ': ' + card.name + ' : ' + str(card.initiative))
            print(card.calcAction(monster))
        print("-"*50)
            
if __name__ == '__main__':
    game = Game(1)
    game.addMonster("AlgoxArcher")
    game.addMonster("AlgoxArcher", elite=1)
    game.addMonster("AlgoxGuard", elite=1)
    game.addMonster("AlgoxScout")
    game.addMonster("AlgoxScout", elite=1)
    game.draw()
    game.draw()
    game.draw()
    game.draw()
    game.draw()