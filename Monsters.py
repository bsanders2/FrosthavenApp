# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:21:16 2023

@author: blake
"""

from numpy.random import shuffle
from copy import copy

class Deck():
    def __init__(self):
        self.deck = []
        
    def addCard(self, modifier_card):
        self.deck.append(modifier_card)
        
    def shuffle(self):
        shuffle(self.deck)
        
    def draw(self):
        # print([x.name for x in self.deck])
        card = self.deck[0]
        self.deck = self.deck[1:]
        self.deck.append(card)
        if card.requires_shuffle:
            self.shuffle()
        return card
        
class ModifierCard:
    def __init__(self, name, initiative, requires_shuffle, move, attack, range, special_text):
        self.name = name
        self.initiative = initiative
        self.requires_shuffle = requires_shuffle
        self.move = move
        self.attack = attack
        self.range = range
        self.special_text = special_text
        
    def __str__(self):
        string = ""
        if self.move:
            string += "Move {}\n".format(self.move)
        if self.attack:
            string += "Attack {}\n".format(self.attack)
        if self.range:
            string += "Range {}\n".format(self.range)
        if self.special_text:
            string += self.special_text+"\n"
        return string
    
    def calcAction(self, Monster):
        action = copy(self)
        # print(action)
        if self.move:
            action.move += Monster.move
        if self.attack:
            action.attack += Monster.attack
        return action

class Monster:
    def __init__(self, level):
        self.level = level
        self.name = ""
        self.health = 0
        self.move = 0
        self.attack = 0
        self.innate = ""
        self.deck = Deck()
        
    def updateProperties(self, level_props, innate=""):
        self.health = level_props[0]
        self.move = level_props[1]
        self.attack = level_props[2]
        self.innate = innate
        
    def draw(self):
        card = self.deck.draw()
        # action = card.calcAction(self)
        return card

        
        
class AlgoxArcher(Monster):
    properties = {0:[[4,1,3],[6,2,4]], 1:[[5,2,3],[8,2,4]]}
    def __init__(self, level, elite=0):
        super().__init__(level)
        self.updateProperties(self.properties[level][elite])
        self.buildDeck()
        self.name = "AlgoxArcher"
        if elite:
            self.name += " Elite"
        
    def buildDeck(self):
        self.deck = Deck()
        self.deck.addCard(ModifierCard("Nothing Special", 31, False, 0, 1, 4, None))
        self.deck.addCard(ModifierCard("Calculated Strike", 44, False, -1, 1, 4, None))
        self.deck.addCard(ModifierCard("Hasty Assault", 16, False, 1, -1, 4, None))
        self.deck.addCard(ModifierCard("Set Trap", 14, False, -1, -1, 5, "Create one 3 damage trap in an adjacent empty hex closest to an enemy"))
        self.deck.addCard(ModifierCard("Shoot Foot", 29, True, 0, -1, 5, "Immobilize"))
        self.deck.addCard(ModifierCard("Close In", 32, False, 0, 1, 3, None))
        self.deck.addCard(ModifierCard("Power Shot", 64, True, None, 1, 5, None))
        self.deck.addCard(ModifierCard("Twin Bolts", 56, False, None, -1, 4, "Target 2"))
        self.deck.shuffle()
        
class AlgoxGuard(Monster):
    properties = {0:[[6,2,3],[10,2,4]], 1:[[7,3,3],[12,3,4]]}
    def __init__(self, level, elite=0):
        super().__init__(level)
        self.updateProperties(self.properties[level][elite])
        self.buildDeck()
        self.name = "AlgoxGuard"
        if elite:
            self.name += " Elite"
        
    def buildDeck(self):
        self.deck = Deck()
        self.deck.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
        self.deck.addCard(ModifierCard("Venom Shiv", 15, False, None, 0, None, "Poison, Shield 1"))
        self.deck.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        self.deck.addCard(ModifierCard("Parry and Thrust", 15, True, None, None, None, "Shield 1, Retaliate 2"))
        self.deck.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        self.deck.addCard(ModifierCard("Psych Up", 55, True, -1, 0, None, "Strengthen Self"))
        self.deck.addCard(ModifierCard("Hasty Assault", 30, False, 1, -1, None, None))
        self.deck.addCard(ModifierCard("Throwing Axe", 35, False, -1, 0, 2, None))
        self.deck.shuffle()
        
class AlgoxScout(Monster):
    properties = {0:[[7,3,2],[10,4,3]], 1:[[8,4,2],[12,4,3]]}   
    def __init__(self, level, elite=0):
        super().__init__(level)
        innate = ""
        if level > 0 and elite:
            innate = "Impair"
        self.updateProperties(self.properties[level][elite], innate)
        self.buildDeck()
        self.name = "AlgoxScout"
        if elite:
            self.name += " Elite"
        
    def buildDeck(self):
        self.deck = Deck()
        self.deck.addCard(ModifierCard("Rapid Bolts", 79, False, None, -1, 4, "Target 2"))
        self.deck.addCard(ModifierCard("Greed", 35, True, 1, None, None, "Loot 1"))
        self.deck.addCard(ModifierCard("Cruel Bow", 29, True, -1, -1, 3, "Impair"))
        self.deck.addCard(ModifierCard("Hasty Assault", 40, False, 1, -1, None, None))
        self.deck.addCard(ModifierCard("Nothing Special", 53, False, 0, 0, None, None))
        self.deck.addCard(ModifierCard("Rancid Arrow", 54, False, -2, 1, 3, "Poison"))
        self.deck.addCard(ModifierCard("Calculated Strike", 69, False, -1, 1, None, None))
        self.deck.addCard(ModifierCard("Noxious Blade", 92, False, None, 2, None, "Poison"))
        self.deck.shuffle()
        
        
        
        
        
        
        
        