# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:39:28 2023

@author: blake
"""

from numpy.random import shuffle


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
        if self.move is not None:
            string += "Move {}\n".format(self.move)
        if self.attack is not None:
            string += "Attack {}\n".format(self.attack)
        if self.range is not None:
            string += "Range {}\n".format(self.range)
        if self.special_text is not None:
            string += self.special_text+"\n"
        return string
    
