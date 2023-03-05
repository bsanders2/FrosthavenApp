# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:21:16 2023

@author: blake
"""

from ModifierCards import ModifierCard, Deck
from copy import copy

class Monster:
    def __init__(self, level, name, elite):
        self.level = level
        self.name = name
        self.elite = elite
        self.health = 0
        self.move = 0
        self.attack = 0
        self.innate = ""
        
    def updateProperties(self, level_props, innate=""):
        self.health = level_props[0]
        self.move = level_props[1]
        self.attack = level_props[2]
        self.innate = innate
        
    def getName(self):
        if self.elite:
            return self.name + " Elite"
        else:
            return self.name
    
    def calcAction(self, card):
        action = copy(card)
        if card.move is not None:
            action.move += self.move
        if card.attack is not None:
            action.attack += self.attack
        return action

        
        
class AlgoxArcher(Monster):
    properties = {0:[[4,1,3],[6,2,4]], 1:[[5,2,3],[8,2,4]]}
    name = "AlgoxArcher"
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite)
        self.updateProperties(self.properties[level][elite])
        
    def buildDeck(self):
        deck = Deck()
        deck.addCard(ModifierCard("Nothing Special", 31, False, 0, 1, 4, None))
        deck.addCard(ModifierCard("Calculated Strike", 44, False, -1, 1, 4, None))
        deck.addCard(ModifierCard("Hasty Assault", 16, False, 1, -1, 4, None))
        deck.addCard(ModifierCard("Set Trap", 14, False, -1, -1, 5, "Create one 3 damage trap in an adjacent empty hex closest to an enemy"))
        deck.addCard(ModifierCard("Shoot Foot", 29, True, 0, -1, 5, "Immobilize"))
        deck.addCard(ModifierCard("Close In", 32, False, 0, 1, 3, None))
        deck.addCard(ModifierCard("Power Shot", 64, True, None, 1, 5, None))
        deck.addCard(ModifierCard("Twin Bolts", 56, False, None, -1, 4, "Target 2"))
        deck.shuffle()
        return deck
        
class AlgoxGuard(Monster):
    properties = {0:[[6,2,3],[10,2,4]], 1:[[7,3,3],[12,3,4]]}
    name = "AlgoxGuard"
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite)
        self.updateProperties(self.properties[level][elite])
        
    def buildDeck(self):
        deck = Deck()
        deck.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
        deck.addCard(ModifierCard("Venom Shiv", 15, False, None, 0, None, "Poison, Shield 1"))
        deck.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        deck.addCard(ModifierCard("Parry and Thrust", 15, True, None, None, None, "Shield 1, Retaliate 2"))
        deck.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        deck.addCard(ModifierCard("Psych Up", 55, True, -1, 0, None, "Strengthen Self"))
        deck.addCard(ModifierCard("Hasty Assault", 30, False, 1, -1, None, None))
        deck.addCard(ModifierCard("Throwing Axe", 35, False, -1, 0, 2, None))
        deck.shuffle()
        return deck
        
class AlgoxScout(Monster):
    properties = {0:[[7,3,2],[10,4,3]], 1:[[8,4,2],[12,4,3]]}  
    name = "AlgoxScout"
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite)
        innate = ""
        if level > 0 and elite:
            innate = "Impair"
        self.updateProperties(self.properties[level][elite], innate)
        
    def buildDeck(self):
        deck = Deck()
        deck.addCard(ModifierCard("Rapid Bolts", 79, False, None, -1, 4, "Target 2"))
        deck.addCard(ModifierCard("Greed", 35, True, 1, None, None, "Loot 1"))
        deck.addCard(ModifierCard("Cruel Bow", 29, True, -1, -1, 3, "Impair"))
        deck.addCard(ModifierCard("Hasty Assault", 40, False, 1, -1, None, None))
        deck.addCard(ModifierCard("Nothing Special", 53, False, 0, 0, None, None))
        deck.addCard(ModifierCard("Rancid Arrow", 54, False, -2, 1, 3, "Poison"))
        deck.addCard(ModifierCard("Calculated Strike", 69, False, -1, 1, None, None))
        deck.addCard(ModifierCard("Noxious Blade", 92, False, None, 2, None, "Poison"))
        deck.shuffle()
        return deck
        
        
        
        
        
        
        
        