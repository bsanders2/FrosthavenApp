# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:31:42 2023

@author: blake
"""
import MonsterNames

from ModifierCards import DeckFactory
from difflib import get_close_matches
import numpy as np

class Game():
    def __init__(self, level):
        self.level = level
        self.monsters = list()
        self.active_monsters = set()
        self.decks = dict()
    
    def addMonster(self, name, elite=0):
        if name in globals():
            obj = globals()[name]
            monster = obj(self.level, elite)
            standee_choices = set(np.arange(1,monster.num_standees+1))
            active_standees = set([m.standee for m in self.monsters if m.name==monster.name])
            print("active_standees ", active_standees)
            standee_choices = standee_choices - active_standees
            if len(standee_choices) == 0:
                return None
            standee = list(standee_choices)[np.random.randint(0, len(standee_choices))]
            monster.standee = standee
            #start here, standees need to be tracked
            self.monsters.append(monster)
            if monster.name not in self.decks.keys():
                self.decks[monster.name] = DeckFactory.buildDeck(monster.deck_name)
            self.active_monsters.add(monster.name)
            return monster
        else:
            print("{} not in Monsters.py, found close match {}".format(name, get_close_matches(name, globals())))
			
    def removeMonster(self, monster):
        for m in self.monsters:
            print(m.name, m.standee, " =? ", (monster.name, monster.standee), (m.name==monster.name, m.standee==monster.standee))
            if m.name==monster.name and m.standee==monster.standee:
                if len([m.name for m in self.monsters if m.name==monster.name]) == 1:
                    print("Setting inactive: ", m.name)
                    # Last monster of that type, stop drawing for it
                    self.active_monsters.remove(m.name)
                self.monsters.remove(m)
                print("removed ", m.name, ': ', m.standee)
                print([(x.name, x.standee) for x in self.monsters])
                return

        print("{} not in self.monsters, found close match {}".format(monster.name, get_close_matches(monster.name, [x.name for x in self.monsters])))
			
    def getMonsterInstance(self, name):
        for m in self.monsters:
            if m.name == name:
                return m
        print("{} is not in monsters".format(name))
            
    def draw(self):
        if len(self.active_monsters) == 0:
            return
        ret = "-"*50+'\n'
        cards = {name : self.decks[name].draw() for name in self.active_monsters}
        monsters = {m.getName() : m for m in self.monsters}
        print("active monsters ", self.active_monsters)
        
        cards, monsters = zip(*sorted(zip([cards[m.name] for m in monsters.values()], monsters.values()), key = lambda x: [x[0].initiative,x[1].getName()]))
        print("cards ", cards)
        print("monsters ", monsters)
        for card, monster in zip(cards, monsters):
            print("card ", card, " monster ", monster)
            ret += monster.getName() + ': ' + card.name + ' : ' + str(card.initiative)+'\n'
            # ret += str(monster.calcAction(card)) +'\n'
            ret += card.calcAction(monster) + '\n'
        ret += "-"*50+'\n'
        return ret
            
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