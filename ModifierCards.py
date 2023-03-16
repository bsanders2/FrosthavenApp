# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:39:28 2023

@author: blake
"""

from numpy.random import shuffle

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
        
class DeckFactory():
    # decks = {
    #     'Archer' : Archer
    #     }
    def __init__(self):
        pass
    
    @staticmethod
    def buildDeck(name):
        return globals()[name]()
    
    
### Deck classes, names may or may not be the same as the Monster class names
### Names here correspond to the deck_name attribute of the Monster class
class Archer(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Nothing Special", 31, False, 0, 1, 4, None))
        self.addCard(ModifierCard("Hasty Assault", 16, False, 1, -1, 4, None))
        self.addCard(ModifierCard("Calculated Strike", 44, False, -1, 1, 4, None))
        self.addCard(ModifierCard("Set Trap", 14, False, -1, -1, 5, "Create one 3 damage trap in an adjacent empty hex closest to an enemy"))
        self.addCard(ModifierCard("Shoot Foot", 29, True, 0, -1, 5, "Immobilize"))
        self.addCard(ModifierCard("Close In", 32, False, 0, 1, 3, None))
        self.addCard(ModifierCard("Power Shot", 64, True, None, 1, 5, None))
        self.addCard(ModifierCard("Twin Bolts", 56, False, None, -1, 4, "Target 2"))
        self.shuffle()
            
class FrozenCorpse(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Nothing Special", 71, True, 0, 0, None, "Infuse Ice"))
        self.addCard(ModifierCard("Frost Breath", 39, True, 0, -1, None, "Infuse Ice, Range 2 Cone"))
        self.addCard(ModifierCard("Cold Snap", 42, False, 1, -1, None, "Confuse Ice -> Cause Brittle"))
        self.addCard(ModifierCard("Thawed Strike", 68, False, -1, 1, None, "Consume Fire -> +2 Move, Suffer 2 damage"))
        self.addCard(ModifierCard("Icy Swipe", 84, False, -1, 1, None, "Infuse Ice, Range 1 Cone"))
        self.addCard(ModifierCard("Thawed Strike", 68, False, -1, 1, None, "Consume Fire -> +2 Move, Suffer 2 damage"))
        self.addCard(ModifierCard("Freezing Embrace", 23, False, 1, None, None, "Brittle, Immobilize, Range 1"))
        self.addCard(ModifierCard("Cold Snap", 42, False, 1, -1, None, "Confuse Ice -> Cause Brittle"))
        self.shuffle()
        
class Guard(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Venom Shiv", 15, False, None, 0, None, "Poison, Shield 1"))
        self.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
        self.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
        self.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        self.addCard(ModifierCard("Parry and Thrust", 15, True, None, None, None, "Shield 1, Retaliate 2"))
        self.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
        self.addCard(ModifierCard("Psych Up", 55, True, -1, 0, None, "Strengthen Self"))
        self.addCard(ModifierCard("Hasty Assault", 30, False, 1, -1, None, None))
        self.addCard(ModifierCard("Throwing Axe", 35, False, -1, 0, 2, None))
        self.shuffle()
        
class IceWraith(Deck):
    def __init__(self):
        super()._init__()
        self.addCard(ModifierCard("Renewed Aggression", 44, True, 0, 0, None, "Heal 1 self, Infuse Ice, (Normal: Range 4)"))
        self.addCard(ModifierCard("Unholy Strength", 59, False, None, 0, 3, "Consume Ice -> Strengthen, Bless self"))
        self.addCard(ModifierCard("Fade Out", 59, False, None, None, None, "Invisible self. Consume Ice -> Strengthen, Bless self. Infuse Ice"))
        self.addCard(ModifierCard("Hasty Assault", 41, False, 1, -1, None, "Infuse Ice, (Normal: Range 4)"))
        self.addCard(ModifierCard("Calculated Strike", 71, False, -1, 1, None, "Infuse Ice, (Normal: Range 4)"))
        self.addCard(ModifierCard("Restore Essence", 13, False, None, None, None, "Heal 3 self. Consume Ice -> Shield 2"))
        self.addCard(ModifierCard("Shard Strike", 16, False, None, 0, None, "(Normal: Range 4). Consume Ice -> Retaliate 2"))
        self.addCard(ModifierCard("Shift Form", 95, True, 0, -1, None, "Change Elite to Normal and vice-versa. Heal 1 self, then move, then Attack (Normal: Range 4)"))
        self.shuffle()
        
class LurkerClawcrusher(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Nothing Special", 47, False, 0, 0, None, "Infuse Earth"))
        self.addCard(ModifierCard("Smash Armor", 58, False, -1, 0, None, "Target suffers damage == their shield. Consume Earth -> Double"))
        self.addCard(ModifierCard("Criplling Claw", 44, False, 0, -1, None, "Poison"))
        self.addCard(ModifierCard("Take Hostage", 13, True, None, -1, None, "Immobilize target. Shield 2. Infuse Earth"))
        self.addCard(ModifierCard("Earthen Blow", 60, True, -1, 1, None, "Consume Earth -> Wound, Poison"))
        self.addCard(ModifierCard("Crush Armor", 36, False, 0, -1, None, "Target suffers damage == their shield. Consume Earth -> Double"))
        self.addCard(ModifierCard("Claw Guard", 11, False, None, None, None, "Shield 2, Retaliate 2, Infuse Earth"))
        self.addCard(ModifierCard("Frantic Swipes", 31, False, 1, -2, None, "Target all adjacent enemies, Poison, Infuse Earth"))
        self.shuffle()
        
class LurkerMindsnipper(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Psychic Shock", 6, True, None, None, None, "Retaliate 3 (Consume Dark->+2), Range 3. Muddle All, Range 3 "))
        self.addCard(ModifierCard("Hasty Assault", 10, False, 2, -1, 3, "Infuse Dark"))
        self.addCard(ModifierCard("Consume All Hope", 22, False, 0, -1, 3, "Curse, Infuse Dark"))
        self.addCard(ModifierCard("Calculated Strike", 34, False, -2, 1, 3, "Infuse Dark"))
        self.addCard(ModifierCard("Instill Fear", 37, False, None, -1, 3, "+2 Target, Push 2"))
        self.addCard(ModifierCard("Beguiling Thoughts", 18, False, 0, -2, 2, "Disarm"))
        self.addCard(ModifierCard("Turn the Weak", 51, True, 0, -2, 3, "Control all targets of attack: Attack 3"))
        self.addCard(ModifierCard("Paralyze", 46, False, None, -1, 4, "Consume Dark -> Stun"))
        self.shuffle()
        
class LurkerSoldier(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Defensive Claws", 11, True, None, None, None, "Wound All, Range 1. Shield 1 (Consume Ice->+1)"))
        self.addCard(ModifierCard("Hasty Assault", 28, False, 1, -1, None, None))
        self.addCard(ModifierCard("Nothing Special", 38, False, 0, 0, None, None))
        self.addCard(ModifierCard("Focused Strikes", 38, False, 0, 0, None, "Target 1 enemy with all attacks"))
        self.addCard(ModifierCard("Calculated Strike", 61, False, -1, 1, None, None))
        self.addCard(ModifierCard("Berserk Rage", 64, False, None, 1, None, "Target enemies within 2 hexes, Impair"))
        self.addCard(ModifierCard("Strength of the Deep", 41, False, 0, -1, None, "First: Consume Ice->Strengthen self. Attack has Wound."))
        self.addCard(ModifierCard("Hardened by Frost", 23, True, 0, -1, None, "Shield 1, Infuse Ice"))
        self.shuffle()
        
class Scout(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Rapid Bolts", 79, False, None, -1, 4, "Target 2"))
        self.addCard(ModifierCard("Greed", 35, True, 1, None, None, "Loot 1"))
        self.addCard(ModifierCard("Cruel Bow", 29, True, -1, -1, 3, "Impair"))
        self.addCard(ModifierCard("Hasty Assault", 40, False, 1, -1, None, None))
        self.addCard(ModifierCard("Nothing Special", 53, False, 0, 0, None, None))
        self.addCard(ModifierCard("Rancid Arrow", 54, False, -2, 1, 3, "Poison"))
        self.addCard(ModifierCard("Calculated Strike", 69, False, -1, 1, None, None))
        self.addCard(ModifierCard("Noxious Blade", 92, False, None, 2, None, "Poison"))
        self.shuffle()
    
