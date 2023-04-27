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

    def __str__(self):
        return self.name
    
    def __repr(self):
        string = self.name+":"+str(self.initiative)+'\n'
        for a in self.actions:
            string += a
        return string
        
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

class BurrowingBlade(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Tunneling Slices", 68, True, actions=["move+1. Jump, Focus farthest enemy away","attack-2. All enemies occupying or adj to move path"]))
        self.addCard(ModifierCard("Tunneling Slices", 68, True, actions=["move+1. Jump, Focus farthest enemy away","attack-2. All enemies occupying or adj to move path"]))
        self.addCard(ModifierCard("Descend", 75, False, actions=["Invisible self", "Infuse Earth"]))
        self.addCard(ModifierCard("Soaring Strikes", 53, False, actions=["move+0. Jump", "attack -1. Target 2", "Infuse Earth"]))
        self.addCard(ModifierCard("Explosive Ascent", 63, False, actions=["move+0. Jump", "All enemies in Range 2 Suffer 2", "Infuse Earth"]))
        self.addCard(ModifierCard("Aura of Fear", 37, False, actions=["move+2. Jump. Focus on farthest enemy away", "Muddle, Curse All, Range 2"]))
        self.addCard(ModifierCard("Rocky Thrust", 65, False, actions=["move-1", "attack+1.\n  Consume Earth->+1"]))
        self.addCard(ModifierCard("Crashing Blow", 85, False, actions=["attack+2.\n  Consume Earth->+2"]))
        self.shuffle()

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

class FlamingBladespinner(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Calculated Strike", 78, False, actions=["move-2", "attack+1. Infuse Fire"]))
        self.addCard(ModifierCard("Spinning Charge", 68, False, actions=["move+1. Jump, Focus farthest enemy away","attack-1. All enemies occupying or adj to move path\n  Consume Fire->Wound"]))
        self.addCard(ModifierCard("Flame Jets", 43, False, actions=["move+2. All enemies in Range 2 Suffer 1", "Consume Fire->Wound All, Range 2"]))
        self.addCard(ModifierCard("Firestorm", 17, False, actions=["Shield 1", "Retaliate 2, Range 3"]))
        self.addCard(ModifierCard("Defensive Blades", 12, False, actions=["Shield 2", "Consume Fire->All enemies in Range 2 Suffer 2"]))
        self.addCard(ModifierCard("Increase Momentum", 33, False, actions=["Moe+0", "attack-1", "Strengthen self. Infuse Fire"]))
        self.addCard(ModifierCard("Hasty Assault", 38, True, actions=["move+2", "attack-1. Infuse Fire"]))
        self.addCard(ModifierCard("Heated Sweep", 58, False, actions=["move+0", "attack+0. Consume Fire->+1, Wound"]))
        self.shuffle()

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
        
class LurkerClawcrusher(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Nothing Special", 47, False, actions=["move+0", "attack+0", "Infuse Earth"]))
        self.addCard(ModifierCard("Smash Armor", 58, False, actions=["move-1", "attack+0. Target Suffers damage equal to their Shield\n  Consume Earth->Double their Shield"]))
        self.addCard(ModifierCard("Cripling Claw", 44, False, actions=["move+0", "attack-1. Poison"]))
        self.addCard(ModifierCard("Take Hostage", 13, True, actions=["attack-1. Immobilize", "Shield 2. Infuse Earth"]))
        self.addCard(ModifierCard("Earthen Blow", 60, True, actions=["move-1", "attack+1.\n  Consume Earth->Wound, Poison"]))
        self.addCard(ModifierCard("Crush Armor", 36, False, actions=["Shield 2", "Retaliate 2", "Infuse Earth"]))
        self.addCard(ModifierCard("Claw Guard", 11, False, actions=["move+0", "attack-1. Target Suffers damage equal to their Shield\n  Consume Earth->Double their Shield"]))
        self.addCard(ModifierCard("Frantic Swipes", 31, False, actions=["move+1", "attack-2. Target all adj enemies, Poison", "Infuse Earth"]))
        self.shuffle()
        
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
        
class LurkerSoldier(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Defensive Claws", 11, True, actions=["Wound All, Range 1", "Shield 1\n  Consume Frost->+1"]))
        self.addCard(ModifierCard("Hasty Assault", 28, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Nothing Special", 38, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Focused Strikes", 38, False, actions=["move+0", "attack+0. Target 1 enemy w/ all attacks"]))
        self.addCard(ModifierCard("Calculated Strike", 61, False, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Berserk Rage", 64, False, actions=["attack+1. Target all enemies in Range 2, Impair"]))
        self.addCard(ModifierCard("Strength of the Deep", 41, False, actions=["Consume Frost->Strengthen self", "move+0", "attack-1. Wound"]))
        self.addCard(ModifierCard("Hardened by Frost", 23, True, actions=["move+0", "attack-1", "Shield 1", "Infuse Frost"]))
        self.shuffle()
        
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
        self.addCard(ModifierCard("The Night Feeds", 15, False, actions=["move+0", "attack-1", "All adjacent enemies and allies Suffer 1 damage", "Consume Any->Infuse Dark"]))
        self.shuffle()
        
class PiranhaPig(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Schooling", 40, True, actions=["move+0", "attack+0. Add +1 if target adj to any PiranhaPig allies"]))
        self.addCard(ModifierCard("Bloodthirst", 38, False, actions=["move+1", "attack-1. Add +2 if target has Wound"]))
        self.addCard(ModifierCard("Easy Prey", 54, False, actions=["move-1", "attack+1. Add +1 if target occupying hex with a water tile"]))
        self.addCard(ModifierCard("Feast", 26, False, actions=["attack+0", "Heal X. X is dmg suffered by target of attack"]))
        self.addCard(ModifierCard("Hasty Assault", 18, False, actions=["move+1. Jump", "attack-1"]))
        self.addCard(ModifierCard("No Escape", 23, False, actions=["attack+1. Immobilize"]))
        self.addCard(ModifierCard("Bared Teeth", 13, False, actions=["move+1. Jump", "Wound All Range 1", "Retaliate 2"]))
        self.addCard(ModifierCard("Nothing Special", 31, False, actions=["move+0", "attack+0"]))
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

class RuinedMachine(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Calculated Strike", 85, False, actions=["move+1","attack+1"]))
        self.addCard(ModifierCard("Hasty Assault", 41, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Signal Jam", 56, True, actions=["move+0", "Muddle All, Range 2. Ruined Machine Suffers 1"]))
        self.addCard(ModifierCard("Nothing Special", 63, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Devastating Tackle", 42, False, actions=["attack+2. Immobilize", "If Attack performed, Suffer 1 self"]))
        self.addCard(ModifierCard("Latch On", 31, False, actions=["move+1", "Poison, Immobilize, Range 1"]))
        self.addCard(ModifierCard("Self-Destruct", 93, True, actions=["move+0", "attack+0", "If Attack performed all adj enemies suffer trap damage. Ruined machine dies."]))
        self.addCard(ModifierCard("Fuel Leak", 29, False, actions=["move+1", "If Attack performed, Suffer 1 self", "attack+0"]))
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
        self.addCard(ModifierCard("Angry Cloud", 9, False, actions=["All enemies in Range 3 Suffer 2 damage", "Retaliate 2 Range 3", "Infuse Dark"]))
        self.addCard(ModifierCard("Gather the Flock", 72, False, actions=["Pull 2, Target All, Range 5", "All enemies in Range 3 Suffer 2 damage"]))
        self.addCard(ModifierCard("Dive Bombs", 49, False, actions=["attack+0. Target 2, Range 3, Immobilize"]))
        self.addCard(ModifierCard("Nothing Special", 90, True, actions=["move+0", "attack+0", "Infuse Dark"]))
        self.addCard(ModifierCard("Birds of Prey", 23, False, actions=["attack-2. Target 3, Range 6, Pull 2", "Consume Dark->Shield 2"]))
        self.shuffle()

class SpittingDrake(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 32, False, actions=["move+1", "attack-1. Range 4"]))
        self.addCard(ModifierCard("Nothing Special", 52, False, actions=["move+0", "attack+0. Range 4"]))
        self.addCard(ModifierCard("Splashing Bile", 57, True, actions=["attack-1. Range 3, AOE Small Triangle"]))
        self.addCard(ModifierCard("Venom Glands", 27, False, actions=["attack+0. Target 2, Range 4, Poison"]))
        self.addCard(ModifierCard("Calculated Strike", 87, False, actions=["Calculated Strike", "move-1", "attack-1. Range 4"]))
        self.addCard(ModifierCard("Subduing Spit", 89, False, actions=["attack-1. Range 4, Stun"]))
        self.addCard(ModifierCard("Empowering Rest", 6, False, actions=["Shield 2", "Heal 2 self, Strengthen self"]))
        self.addCard(ModifierCard("Explosive Vomit", 89, True, actions=["move-1", "attack-2. Range 3, Poison, AOI Flower"]))
        self.shuffle()

class SteelAutomaton(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Calculated Strike", 95, True, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Heavy Footfalls", 48, False, actions=["Adj enemies Suffer 1", "move+2", "Adj enemies Suffer Hazardous Terrain dmg"]))
        self.addCard(ModifierCard("Clobber", 76, False, actions=["attack+1. Stun"]))
        self.addCard(ModifierCard("Body Block", 24, False, actions=["move+1", "Shield 1, Retaliate 2"]))
        self.addCard(ModifierCard("Nothing Special", 70, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Mortar Shell", 64, False, actions=["attack-1. Range 3, Pierce 3"]))
        self.addCard(ModifierCard("Unstoppable Force", 45, False, actions=["move+1", "attack-1. Push 3"]))
        self.addCard(ModifierCard("Immovable Object", 10, True, actions=["Shield 4"]))
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
    

    

    

    