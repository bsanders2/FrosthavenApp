# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:39:28 2023

@author: blake
"""

from numpy.random import shuffle
from MonsterNames import importClasses
monster_classes = importClasses()

class ModifierCard:
    def __init__(self, name, initiative, requires_shuffle, actions):
        self.name = name
        self.initiative = initiative
        self.requires_shuffle = requires_shuffle
        self.actions = actions
        
    def calcAction(self, monster):
        string = ""
        for action in self.actions:
            a = action.split(".")
            if "move" in a[0]:
                mod = int(a[0].lstrip("move"))
                string += "Move " + str(monster.move+mod)
            elif "attack" in a[0]:
                mod = int(a[0].lstrip("attack"))
                string += "Attack " + str(monster.attack+mod)
            else:
                string += a[0] + "\n"
            if len(a) > 1:
                for s in a[1:]:
                    string += s + "\n"
            if string[-1] != "\n":
                string += "\n"
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
        deck_name = monster_classes[name].deck_name
        return globals()[deck_name]()
    
    
### Deck classes, names may or may not be the same as the Monster class names
### Names here correspond to the deck_name attribute of the Monster class
# class Archer(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Nothing Special", 31, False, 0, 1, 4, None))
#         self.addCard(ModifierCard("Hasty Assault", 16, False, 1, -1, 4, None))
#         self.addCard(ModifierCard("Calculated Strike", 44, False, -1, 1, 4, None))
#         self.addCard(ModifierCard("Set Trap", 14, False, -1, -1, 5, "Create one 3 damage trap in an adjacent empty hex closest to an enemy"))
#         self.addCard(ModifierCard("Shoot Foot", 29, True, 0, -1, 5, "Immobilize"))
#         self.addCard(ModifierCard("Close In", 32, False, 0, 1, 3, None))
#         self.addCard(ModifierCard("Power Shot", 64, True, None, 1, 5, None))
#         self.addCard(ModifierCard("Twin Bolts", 56, False, None, -1, 4, "Target 2"))
#         self.shuffle()
        
# class DeepTerror(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Horrible Glare", 65, False, actions=["attack-1. Target 3, Range 3, Curse"]))
#         self.addCard(ModifierCard("Beam of Annihilation", 60, True, actions=["attack+0. Pierce 3, 5 Hex AOE Line"]))
#         self.addCard(ModifierCard("Beam of Annihilation", 60, True, actions=["attack+0. Pierce 3, 5 Hex AOE Line"]))
#         self.addCard(ModifierCard("Burning Gaze", 84, False, actions=["attack-1. Target all adjacent enemies", "attack+0. Range 4, Wound"]))
#         self.addCard(ModifierCard("Rooted Fear", 75, False, actions=["attack-1. Poison", "attack-1. Range 5, Immobilize"]))
#         self.addCard(ModifierCard("Disruptive Frenzy", 75, False, actions=["attack-2. Disarm", "attack-1. Target 2, Range 3, Impair"]))
#         self.addCard(ModifierCard("Terrible Growth", 96, False, actions=["attack-2. Range 6\n  Summon normal deep terror adjacent to target"]))
#         self.addCard(ModifierCard("Ray of Hate", 54, False, actions=["Wound, Poison, Target all enemies in Range 1", "attack+0. Range 4"]))
#         self.shuffle()

# class FrozenCorpse(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Nothing Special", 71, True, 0, 0, None, "Infuse Ice"))
#         self.addCard(ModifierCard("Frost Breath", 39, True, 0, -1, None, "Infuse Ice, Range 2 Cone"))
#         self.addCard(ModifierCard("Cold Snap", 42, False, 1, -1, None, "Confuse Ice -> Cause Brittle"))
#         self.addCard(ModifierCard("Thawed Strike", 68, False, -1, 1, None, "Consume Fire -> +2 Move, Suffer 2 damage"))
#         self.addCard(ModifierCard("Icy Swipe", 84, False, -1, 1, None, "Infuse Ice, Range 1 Cone"))
#         self.addCard(ModifierCard("Thawed Strike", 68, False, -1, 1, None, "Consume Fire -> +2 Move, Suffer 2 damage"))
#         self.addCard(ModifierCard("Freezing Embrace", 23, False, 1, None, None, "Brittle, Immobilize, Range 1"))
#         self.addCard(ModifierCard("Cold Snap", 42, False, 1, -1, None, "Consume Ice -> Cause Brittle"))
#         self.shuffle()
        
# class Guard(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Venom Shiv", 15, False, None, 0, None, "Poison, Shield 1"))
#         self.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
#         self.addCard(ModifierCard("Calculated Strike", 70, False, -1, 1, None, None))
#         self.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
#         self.addCard(ModifierCard("Parry and Thrust", 15, True, None, None, None, "Shield 1, Retaliate 2"))
#         self.addCard(ModifierCard("Nothing Special", 50, False, 0, 0, None, None))
#         self.addCard(ModifierCard("Psych Up", 55, True, -1, 0, None, "Strengthen Self"))
#         self.addCard(ModifierCard("Hasty Assault", 30, False, 1, -1, None, None))
#         self.addCard(ModifierCard("Throwing Axe", 35, False, -1, 0, 2, None))
#         self.shuffle()
        
class HarrowerInfester(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Biting Gnats", 38, False, actions=["move-1", "attack+1. Target 2"]))
        self.addCard(ModifierCard("Centipede Strike", 7, False, actions=["move+0", "attack-1. Poison", "Infuse Dark"]))
        self.addCard(ModifierCard("Restore the Swarm", 16, False, actions=["move-1", "attack-1", "Heal 5 self"]))
        self.addCard(ModifierCard("Drain the Essence", 7, True, actions=["attack-1. Range 3, Muddle", "Heal 4 self"]))
        self.addCard(ModifierCard("Spiked Mandibles", 16, False, actions=["attack+2. Immobilize", "Retaliate 2"]))
        self.addCard(ModifierCard("Angry Bulwark", 2, True, actions=["Shield 2", "Retaliate 2, Range 3"]))
        self.addCard(ModifierCard("Piercing Parasites", 30, False, actions=["move-1", "attack+0. 3 Hex AOE Line\n  Consume Dark->Heal 2xNum Targeted"]))
        self.addCard(ModifierCard("Clouds of Hate", 38, False, actions=["move+0", "attack-1. Target 2, Impair\n  Consume Dark->+1 Attack"]))
        self.shuffle()

class Hound(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Gripping Teeth", 6, False, actions=["move-1", "attack+0. Immobilize"]))
        self.addCard(ModifierCard("Harrowing Howl", 7, False, actions=["move+0", "Muddle all, Range 1"]))
        self.addCard(ModifierCard("Pack Hunting", 19, True, actions=["move+0", "attack+0. Add +2 if target adj. to any of Hound's allies"]))
        self.addCard(ModifierCard("Pack Hunting", 19, True, actions=["move+0", "attack+0. Add +2 if target adj. to any of Hound's allies"]))
        self.addCard(ModifierCard("Nothing Special", 26, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Nothing Special", 26, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Calculated Strike", 83, False, actions=["move-2", "attack+1"]))
        self.addCard(ModifierCard("Sharp Fangs", 72, False, actions=["attack-1. Pierce 2", "move-2", "attack-1. Pierce 2"]))
        self.shuffle()
                                 
class IceWraith(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Shift Form", 95, True, actions=["Swap Elite and Normal", "Heal 1 self", "move+0", "attack-1. (Normal Range 4)"]))
        self.addCard(ModifierCard("Shard Strike", 16, False, actions=["attack+0. (Normal Range 4)", "Consume Ice->Retaliate 2"]))
        self.addCard(ModifierCard("Restore Essence", 13, False, actions=["Heal 3", "Consume Ice->Shield 2"]))
        self.addCard(ModifierCard("Calculated Strike", 71, False, actions=["move-1", "attack+1. (Normal Range 4)", "Infuse Ice"]))
        self.addCard(ModifierCard("Hasty Assault", 41, False, actions=["move+1", "attack-1. (Normal Range 4)", "Infuse Ice"]))
        self.addCard(ModifierCard("Fade Out", 59, False, actions=["Invisible self", "Consume Ice->Strengthen, Bless self", "Infuse Ice"]))
        self.addCard(ModifierCard("Unholy Strength", 59, False, actions=["Consume Ice->Strengthen, Bless self", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Renewed Aggression", 44, True, actions=["Heal 1 self", "move+0", "attack+0. (Normal Range 4)", "Infuse Ice"]))
        self.shuffle()
        
class Imp(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Phase Out", 5, False, actions=["Shield 5", "Heal 1 self", "Infuse Random"]))
        self.addCard(ModifierCard("Nothing Special", 37, False, actions=["move+0", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Nothing Special", 37, False, actions=["move+0", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Restoration", 42, False, actions=["move+1", "Heal 2, Range 3"]))
        self.addCard(ModifierCard("Rotten Sting", 43, True, actions=["move+0", "attack-1. Range 3, Poison\n  Consume Random->+1 Target"]))
        self.addCard(ModifierCard("Calculated Strike", 76, False, actions=["move-1", "attack+1. Range 3"]))
        self.addCard(ModifierCard("Dark Charm", 43, True, actions=["move+0", "attack-1. Range 3, Curse\n  Consume Random->+1 Target"]))
        self.addCard(ModifierCard("Tip the Scales", 24, False, actions=["Strengthen allies, Range 2", "Muddle enemies, Range 2"]))
        self.shuffle()
        
# class LurkerClawcrusher(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Nothing Special", 47, False, 0, 0, None, "Infuse Earth"))
#         self.addCard(ModifierCard("Smash Armor", 58, False, -1, 0, None, "Target suffers damage == their shield. Consume Earth -> Double"))
#         self.addCard(ModifierCard("Criplling Claw", 44, False, 0, -1, None, "Poison"))
#         self.addCard(ModifierCard("Take Hostage", 13, True, None, -1, None, "Immobilize target. Shield 2. Infuse Earth"))
#         self.addCard(ModifierCard("Earthen Blow", 60, True, -1, 1, None, "Consume Earth -> Wound, Poison"))
#         self.addCard(ModifierCard("Crush Armor", 36, False, 0, -1, None, "Target suffers damage == their shield. Consume Earth -> Double"))
#         self.addCard(ModifierCard("Claw Guard", 11, False, None, None, None, "Shield 2, Retaliate 2, Infuse Earth"))
#         self.addCard(ModifierCard("Frantic Swipes", 31, False, 1, -2, None, "Target all adjacent enemies, Poison, Infuse Earth"))
#         self.shuffle()
        
# class LurkerMindsnipper(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Psychic Shock", 6, True, None, None, None, "Retaliate 3 (Consume Dark->+2), Range 3. Muddle All, Range 3 "))
#         self.addCard(ModifierCard("Hasty Assault", 10, False, 2, -1, 3, "Infuse Dark"))
#         self.addCard(ModifierCard("Consume All Hope", 22, False, 0, -1, 3, "Curse, Infuse Dark"))
#         self.addCard(ModifierCard("Calculated Strike", 34, False, -2, 1, 3, "Infuse Dark"))
#         self.addCard(ModifierCard("Instill Fear", 37, False, None, -1, 3, "+2 Target, Push 2"))
#         self.addCard(ModifierCard("Beguiling Thoughts", 18, False, 0, -2, 2, "Disarm"))
#         self.addCard(ModifierCard("Turn the Weak", 51, True, 0, -2, 3, "Control all targets of attack: Attack 3"))
#         self.addCard(ModifierCard("Paralyze", 46, False, None, -1, 4, "Consume Dark -> Stun"))
#         self.shuffle()
        
# class LurkerSoldier(Deck):
#     def __init__(self):
#         super().__init__()
#         self.addCard(ModifierCard("Defensive Claws", 11, True, None, None, None, "Wound All, Range 1. Shield 1 (Consume Ice->+1)"))
#         self.addCard(ModifierCard("Hasty Assault", 28, False, 1, -1, None, None))
#         self.addCard(ModifierCard("Nothing Special", 38, False, 0, 0, None, None))
#         self.addCard(ModifierCard("Focused Strikes", 38, False, 0, 0, None, "Target 1 enemy with all attacks"))
#         self.addCard(ModifierCard("Calculated Strike", 61, False, -1, 1, None, None))
#         self.addCard(ModifierCard("Berserk Rage", 64, False, None, 1, None, "Target enemies within 2 hexes, Impair"))
#         self.addCard(ModifierCard("Strength of the Deep", 41, False, 0, -1, None, "First: Consume Ice->Strengthen self. Attack has Wound."))
#         self.addCard(ModifierCard("Hardened by Frost", 23, True, 0, -1, None, "Shield 1, Infuse Ice"))
#         self.shuffle()
        
class NightDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 4, False, actions=["move+1", "attack-1", "Infuse Dark"]))
        self.addCard(ModifierCard("Into Darkness", 37, False, actions=["move+1", "attack-2", "Consume Dark->Invisible self"]))
        self.addCard(ModifierCard("Nothing Special", 22, False, actions=["move+0", "attack+0", "Infuse Dark"]))
        self.addCard(ModifierCard("Black Thorns", 26, False, actions=["attack-2. Target 3, Range 3\n  Consume Dark->Muddle"]))
        self.addCard(ModifierCard("Death's Embrace", 46, True, actions=["move-1", "attack+1.\n  Consume Dark->+2 Attack"]))
        self.addCard(ModifierCard("Calculated Strike", 41, True, actions=["move-1", "attack+1", "Infuse Dark"]))
        self.addCard(ModifierCard("Impale", 35, False, actions=["attack-1", "attack-1. Pierce 2", "Consume Light->Curse self"]))
        self.addCard(ModifierCard("The Night Feeds", 15, False, actions=["move+0", "attack-1", "All adjacent enemies and allies suffer 1 damage", "Consume Any->Infuse Dark"]))
        self.shuffle()
        
class Priest(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Divine Energy", 89, False, actions=["move-1", "Heal 1, Range 1, Target All Allies", "Bless self"]))
        self.addCard(ModifierCard("Tend to the Clan", 23, True, actions=["move+0", "Heal 3 Range 3"]))
        self.addCard(ModifierCard("Drain Strength", 8, False, actions=["move+0", "attack-1. Disarm"]))
        self.addCard(ModifierCard("Drain Speed", 8, False, actions=["move-1", "attack0. Range 3, Immobilize"]))
        self.addCard(ModifierCard("Tend to the Clan", 23, True, actions=["move+0", "Heal 3 Range 3"]))
        self.addCard(ModifierCard("Calculated Strike", 74, False, actions=["move-1", "attack+1. Range 3"]))
        self.addCard(ModifierCard("Angry Hex", 9, False, actions=["move+1", "attack-1. Target 2, Range 3, Curse"]))
        self.addCard(ModifierCard("Nothing Special", 62, False, actions=["move+0", "attack+0. Range 3"]))
        self.shuffle()
        
class PolarBear(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 13, True, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Hibernate", 3, False, actions=["Shield 1", "Retaliate 2", "Heal 2 self"]))
        self.addCard(ModifierCard("Low Slash", 14, False, actions=["move-1", "attack-1. Immobilize"]))
        self.addCard(ModifierCard("Full Force",29, False, actions=["attack+1. Immobilize"]))
        self.addCard(ModifierCard("Nothing Special", 41, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Claw Swipes", 61, False, actions=["move+0", "attack-1. Target 2"]))
        self.addCard(ModifierCard("Calculated Strike", 60, False, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Rampage", 80, True, actions=["attack-1", "move-2", "attack-1. Impair"]))
        self.shuffle()
        
class Scout(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Noxious Blade", 92, False, actions=["attack+2. Poison"]))
        self.addCard(ModifierCard("Calculated Strike", 69, False, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Rancid Arrow", 54, False, actions=["move-2", "attack+0. Range 3, Poison"]))
        self.addCard(ModifierCard("Nothing Special", 53, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Hasty Assault", 40, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Cruel Bow",  29, True, actions=["move-1", "attack-1. Range 3, Impair"]))
        self.addCard(ModifierCard("Greed", 35, False, actions=["move+1. Jump", "Loot 1"]))
        self.addCard(ModifierCard("Rapid Bolts", 79, False, actions=["attack-1. Target 2, Range 4"]))
        self.shuffle()
        
class ShrikeFiend(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Darken The Skies", 27, False, actions=["move+0", "attack-1. Target 3, Range 3"]))
        self.addCard(ModifierCard("Concentrated Flock", 10, True, actions=["move-1", "attack+0. Target 2, Range 5"]))
        self.addCard(ModifierCard("Fiendish Charge", 73, False, actions=["move+2", "attack+0. Push 2"]))
        self.addCard(ModifierCard("Angry Cloud", 9, False, actions=["All enemies in range 3 suffer 2 damage", "Retaliate 2 Range 3", "Infuse Dark"]))
        self.addCard(ModifierCard("Gather the Flock", 72, False, actions=["Pull 2, Target All, Range 5", "All enemies in range 3 suffer 2 damage"]))
        self.addCard(ModifierCard("Dive Bombs", 49, False, actions=["attack+0. Target 2, Range 3, Immobilize"]))
        self.addCard(ModifierCard("Nothing Special", 90, True, actions=["move+0", "attack+0", "Infuse Dark"]))
        self.addCard(ModifierCard("Birds of Prey", 23, False, actions=["attack-2. Target 3, Range 6, Pull 2", "Consume Dark->Shield 2"]))
        self.shuffle()
    
class WindDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Into Thin Air", 9, False, actions=["attack-1. Range 2", "Heal 1 self", "Consume Wind->Invisible self"]))
        self.addCard(ModifierCard("Tailwind", 21, True, actions=["move+0", "attack+0. Range 3, Pull 1", "Infuse Wind"]))
        self.addCard(ModifierCard("Tailwind", 21, True, actions=["move+0", "attack+0. Range 3, Pull 1", "Infuse Wind"]))
        self.addCard(ModifierCard("Whirlwinds", 29, False, actions=["move+0", "attack-1. Target 2, Range 3\n  Consume Wind->Push 2"]))
        self.addCard(ModifierCard("Cyclone", 37, False, actions=["move+0", "attack+0. Small melee triangle\n  Consume Wind->+1 attack, bigger area"]))
        self.addCard(ModifierCard("Cutting Blast", 43, False, actions=["move-1", "attack+1. Range 3\n  Consume Wind->Disarm"]))
        self.addCard(ModifierCard("Blast of Air", 43, False, actions=["Push 1, Target all, Range 1", "attack+0. Range 4, Disarm\n  Consume Earth->-2 Range"]))
        self.addCard(ModifierCard("Eye of the Storm", 2, False, actions=["move-1", "attack-1. Range 3", "Shield 1", "Consume Any->Infuse Wind"]))
        self.shuffle()
    

    

    

    