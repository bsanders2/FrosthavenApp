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
            for a in action.split("."):
                if a.find("move") == 0:
                    mod = int(a.lstrip("move"))
                    string += "Move " + str(monster.move+mod)
                elif a.find("attack") == 0:
                    mod = int(a.lstrip("attack"))
                    string += "Attack " + str(monster.attack+mod)
                else:
                    string += a
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

class AbaelHerder(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Briny Bristles", 18, False, actions=["move-1", "Grant closest Piranha Pig within Range 5->\n Move+0\n Attack+1"]))
        self.addCard(ModifierCard("Desperate Herd", 72, False, actions=["move-1", "Grant all Piranha Pigs within Range 3\n Move-2\n Attack-2, Piranha Pig suffers 1 damage"]))
        self.addCard(ModifierCard("Pig Parade", 68, True, actions=["Summon one normal Piranha Pig"]))
        self.addCard(ModifierCard("Fish Net", 20, False, actions=["move+0", "attack+0. Range 3, Pull 2, Immobilize"]))
        self.addCard(ModifierCard("Advancing Horde", 88, False, actions=["Grant closest Piranha Pig within Range 4\n Move+0\n Attack+0, Muddle", "If no Piranha Pig was targeted, summon one normal Piranha Pig"]))
        self.addCard(ModifierCard("Guide the School", 12, False, actions=["attack+0. Range 3", "Strengthen all Piranha Pigs, Range 3"]))
        self.addCard(ModifierCard("Heed The Pigs", 65, True, actions=["move+0", "Attack X, X is number of Piranha Pigs on the map"]))
        self.addCard(ModifierCard("Nothing Special", 56, False, actions=["move+0", "attack+0. Range 3"]))
        self.shuffle()

class AlgoxIcespeaker(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Warding Swipe", 17, True, actions=["move+1", "attack-1. Target 4 adj spaces next to each other", "Shield 1, Infuse Earth"]))
        self.addCard(ModifierCard("Knockout Punch", 76, False, actions=["move+0", "attack-1. Stun", "Infuse Frost"]))
        self.addCard(ModifierCard("Two-Fisted Strike", 41, False, actions=["move-1", "attack-1.\n Consume Frost->+2", "attack-1.\n Consume Earth->+2"]))
        self.addCard(ModifierCard("Frozen Debris", 39, False, actions=["move-1", "attack+0. Range 3\n Consume Frost->Immobilize"]))
        self.addCard(ModifierCard("Ice Wall", 8, False, actions=["Create 1 hex obtacle adj to enemy", "All enemies adj to the obstacle suffer hazardous terrain damage", "Infuse Frost and Earth"]))
        self.addCard(ModifierCard("Nothing Special", 56, True, actions=["move+0", "attack+0","Infuse Earth"]))
        self.addCard(ModifierCard("Terrifying Growl", 80, False, actions=["attack+0", "Disarm all, Range 2"]))
        self.addCard(ModifierCard("One with the Earth", 12, False, actions=["Shield 3", "Consume Earth->Heal 1 self", "Heal 3 self"]))
        self.shuffle()

class AlgoxSnowspeaker(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Blinding Vortex", 22, False, actions=["move+0", "attack-1. Range 3, Muddle, Flower AOE", "Infuse Wind"]))
        self.addCard(ModifierCard("Cold Winds", 18, False, actions=["attack+0. Target 2, Range 5\n Consume Frost->Immobilize"]))
        self.addCard(ModifierCard("Sleet", 43, False, actions=["move+0", "attack+1. Range 4", "Infuse Frost"]))
        self.addCard(ModifierCard("Blistering Assault", 30, False, actions=["move+0", "attack-1. Range 4, Push 1\n Consume Wind->+2 Push"]))
        self.addCard(ModifierCard("Snowstorm", 6, True, actions=["All enemies in Range 3 suffer 2 damage", "Push 2, Target all, Range 3", "Infuse Frost, Infuse Wind"]))
        self.addCard(ModifierCard("Hail", 59, False, actions=["move-1", "attac+1. Range 5\n Consume Frost->+2"]))
        self.addCard(ModifierCard("Nothing Special", 27, False, actions=["Move+0", "attack+0", "Infuse Wind"]))
        self.addCard(ModifierCard("Snow Drifts", 66, False, actions=["Immobilize all, Range 6", "Consume Wind->Muddle all, Range 6"]))
        self.shuffle()

class AncientArtillery(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Exploding Ammunition", 71, True, actions=["attack+0. Range 5, All enemies adj to target suffer 2 damage"]))
        self.addCard(ModifierCard("Grenade", 37, False, actions=["Push 1, Target all, Range 1", "attack-1. Range 4, small triangle AOE"]))
        self.addCard(ModifierCard("Heavy Shot", 95, False, actions=["attack+1. Range 5"]))
        self.addCard(ModifierCard("Concussive Burst", 46, False, actions=["attack-1. Range 5, Immobilize, small triangle AOE"]))
        self.addCard(ModifierCard("Long Shot", 46, False, actions=["Focus enemy farthest away within Range 7", "attack-1. Range 7"]))
        self.addCard(ModifierCard("Exploding Ammunition", 71, True, actions=["attack+0. Range 5, All enemies adj to target suffer 2 damage"]))
        self.addCard(ModifierCard("Massive Blast", 57, False, actions=["Push 1, Target all, Range 1", "attack-1. Range 3, large flower AOE"]))
        self.addCard(ModifierCard("Defensive Ordinance", 17, False, actions=["Push 2, Target all, Range 1", "attack-2. Range 5", "Shield 2"]))
        self.shuffle()

class Archer(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 16, False, actions=["move+1", "attack-1. Range 4"]))
        self.addCard(ModifierCard("Nothing Special", 31, False, actions=["move+0", "attack+0. Range 4"]))
        self.addCard(ModifierCard("Calculated Strike", 44, False, actions=["move-1", "attack+1. Range 4"]))
        self.addCard(ModifierCard("Twin Bolts", 56, False, actions=["attack+1. Target 2, Range 4"]))
        self.addCard(ModifierCard("Power Shot", 64, True, actions=["attack+1. Range 5"]))
        self.addCard(ModifierCard("Close In", 32, False, actions=["move+0", "attack+1. Range 3"]))
        self.addCard(ModifierCard("Shoot Foot", 29, True, actions=["move+0", "attack-1. Range 5, Immobilize"]))
        self.addCard(ModifierCard("Set Trap", 14, False, actions=["move-1", "attack-1. Range 5", "Create one 3 damage trap in an adj empty hex closest to an enemy"]))
        self.shuffle()

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

class ChaosDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Chilling Breath", 14, False, actions=["move-1.", "attack+0. 2 adj Hex melee AOE", "Consume Frost->Retaliate 2, Range 2"]))
        self.addCard(ModifierCard("Heat Blast", 1, False, actions=["move+1", "attack-1. Range 2\n  Consume Fire->Wound"]))
        self.addCard(ModifierCard("Seismic Punch", 67, False, actions=["move-2.", "attack+1. Push 2\n  Consume Earth->2 adj Hex Melee AOE"]))
        self.addCard(ModifierCard("Whirlwind", 20, False, actions=["move+0", "attack-1. Range 2, small triangle AOE", "Consume Wind->Shield 2"]))
        self.addCard(ModifierCard("White Claws", 42, False, actions=["move+0", "attack+0. Advantage", "Consume Light->Heal 4 self"]))
        self.addCard(ModifierCard("Black Tendrils", 51, False, actions=["move-1", "attack+1", "Consume Dark->Invisible self"]))
        self.addCard(ModifierCard("Arcane Explosion", 77, True, actions=["move+0", "attack+0", "Infuse All Elements"]))
        self.addCard(ModifierCard("Hungry Maw", 98, True, actions=["move-1", "attack-1.\n  Consume Any->Apply Bane"]))
        self.shuffle()
        

class DeepTerror(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Ray of Heat", 54, False, actions=["Wound, Poison, Target all Range 1", "attack+0. Range 4"]))
        self.addCard(ModifierCard("Terrible Growth", 96, False, actions=["attack-2. Range6 \n If attack was performed, summon one normal Deep Terror in empty hex adj to target"]))
        self.addCard(ModifierCard("Disruptive Frenzy", 75, False, actions=["attack-2. Disarm", "attack-1. Target 2, Range 3, Impiar"]))
        self.addCard(ModifierCard("Rooted Fear", 75, False, actions=["attack-1. Poison", "attack-1. Range 5, Immobilize"]))
        self.addCard(ModifierCard("Burning Gaze", 84, False, actions=["attack-1. Target all adj enemies", "attack+0. Range 5, Wound"]))
        self.addCard(ModifierCard("Beam of Annihilation", 60, True, actions=["attack+0. Pierce 2, Line AoE 5 hexes in front"]))
        self.addCard(ModifierCard("Beam of Annihilation", 60, True, actions=["attack+0. Pierce 2, Line AoE 5 hexes in front"]))
        self.addCard(ModifierCard("Horrible Glare", 65, False, actions=["attack-1. Range 3, Target 3, Curse"]))
        self.addCard(ModifierCard("Ray of Hate", 54, False, actions=["Wound, Poison all, Range 1", "attack+0. Range 4"]))
        self.shuffle()

class EarthDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 42, True, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Nothing Special", 62, False, actions=["move+0", "attack+0", "Infuse Earth"]))
        self.addCard(ModifierCard("Boulder Throw", 71, False, actions=["attack+0. Range 4\n Consume Earth->+1 Target"]))
        self.addCard(ModifierCard("Calculated Strike", 83, False, actions=["move-1", "attack+1", "Infuse Earth"]))
        self.addCard(ModifierCard("Ground Slam", 93, False, actions=["move-1", "attack-1. Target all adj enemies\n Consume Earth->Push 1"]))
        self.addCard(ModifierCard("Reckless Charge", 79, False, actions=["move+1", "attack+0.\n Consume Wind->(-)2"]))
        self.addCard(ModifierCard("Earthen Eruption", 87, False, actions=["move+0", "attack-1. Little triangle adj AoE\n Consume Any->Infuse Earth"]))
        self.addCard(ModifierCard("Strong Growth", 40, True, actions=["Heal 4 self", "Consume Earth->Immobilize all, Range 2"]))
        self.shuffle()
        
class FlameDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Intense Torch", 49, False, actions=["attack+0. 2 hex line AoE\n Consume Fire->+1 damage, Wound"]))
        self.addCard(ModifierCard("Heat Aura", 77, False, actions=["attack+0. Target all adj enemies", "Consume Frost->take 1 damage"]))
        self.addCard(ModifierCard("Nothing Special", 24, False, actions=["move+0", "attack+0. Range 4", "Infuse Fire"]))
        self.addCard(ModifierCard("Raging Blaze", 30, True, actions=["Consume Fire->All adj enemies suffer 1 damage", "move+0", "attack-2. Target 2, Range 4, Wound"]))
        self.addCard(ModifierCard("Fire Spout", 8, False, actions=["move-1", "Create one 4 damage trap in adj hex closest to enemy", "Consume Any->Infuse Fire"]))
        self.addCard(ModifierCard("Calculated Strike", 67, False, actions=["move-1", "attack+1. Range 3", "Infuse Fire"]))
        self.addCard(ModifierCard("Explosive Blast", 46, True, actions=["attack+0. Range 5\n Consume Fire->Large flower and -1 Range"]))
        self.addCard(ModifierCard("Hasty Assault", 3, False, actions=["move+1", "attack-1. Range 4", "Infuse Fire"]))
        self.shuffle()

class FrostDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Intense Torch", 49, False, actions=["Immobilize all, Range 2", "Consume Frost-> Heal 3 self"]))
        self.addCard(ModifierCard("Hasty Assault", 38, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Frozen Shards", 58, False, actions=["move-1", "attack+0. Range 2\n Consume Frost->+2 attack, +1 Range"]))
        self.addCard(ModifierCard("Nothing Special", 58, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Cold Claws", 78, True, actions=["move-1", "attack+0. 2 Hex melee AoE adjacent Hex"]))
        self.addCard(ModifierCard("Cold Claws", 78, True, actions=["move-1", "attack+0. 2 Hex melee AoE adjacent Hex"]))
        self.addCard(ModifierCard("Chilld to the Bone", 58, False, actions=["move-1", "attack-1. Pierce 3\n Consume any->Infuse Frost"]))
        self.addCard(ModifierCard("Ice Barrier", 18, False, actions=["move+1", "Shield 2", "Consume Fire->1 damage self"]))
        self.shuffle()

class FrozenCorpse(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Cold Snap", 42, False, actions=["move+1", "attack-1.\n Consume Frost->Brittle"]))
        self.addCard(ModifierCard("Thawed Strike", 68, False, actions=["move-1.\n Consume Fire->+2 move\n If the element is consumed by the move, suffer 2 damage", "attack+1"]))
        self.addCard(ModifierCard("Freezing Embrace", 23, False, actions=["move+1", "Brittle, Immobilize, Range 1"]))
        self.addCard(ModifierCard("Thawed Strike", 68, False, actions=["move-1.\n Consume Fire->+2 move\n If the element is consumed by the move, suffer 2 damage", "attack+1"]))
        self.addCard(ModifierCard("Frost Breath", 39, True, actions=["move+0", "attack-1. Melee Cone AoE (1)x2x3", "Infuse Ice"]))
        self.addCard(ModifierCard("Cold Snap", 42, False, actions=["move+1", "attack-1.\n Consume Frost->Brittle"]))
        self.addCard(ModifierCard("Nothing Special", 71, True, actions=["move+0", "attack+0", "Infuse Frost"]))
        self.addCard(ModifierCard("Icy Swipe", 84, False, actions=["move-1", "attack+1. Melee 2 taget Aoe Adj", "Infuse Frost"]))
        self.shuffle()     

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

class Guard(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Throwing Axe", 35, False, actions=["move-1", "attack+0. Range 2"]))
        self.addCard(ModifierCard("Hasty Assault", 30, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Psych Up", 55, True, actions=["move-1", "attack+0", "Strengthen Self"]))
        self.addCard(ModifierCard("Nothng Special", 50, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Parry and Trust", 15, True, actions=["Shield 1", "Retaliate 2"]))
        self.addCard(ModifierCard("Nothing Special", 50, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Venom Shiv", 15, False, actions=["move+0. Poison", "Shield 1"]))
        self.addCard(ModifierCard("Calculated Strike", 70, False, actions=["move-1", "attack+1"]))
        self.shuffle()

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
        self.addCard(ModifierCard("Pack Hunting", 19, True, actions=["move+0", "attack+0. Add +2 if target adj to any of Hound's allies"]))
        self.addCard(ModifierCard("Pack Hunting", 19, True, actions=["move+0", "attack+0. Add +2 if target adj to any of Hound's allies"]))
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

class LightningEel(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Nothing Special", 20, False, actions=["move+0", "attack+0", "Infuse Light"]))
        self.addCard(ModifierCard("Shocking Voltage", 82, True, actions=["move-1", "attack-1. Target all adj enemies\n Consume Light->Stun"]))
        self.addCard(ModifierCard("Thrasing in the Water", 9, True, actions=["move+1", "attack-1. Target all adj enemies"]))
        self.addCard(ModifierCard("Calculated Strike", 35, False, actions=["move-1", "attack+1", "Infuse Light"]))
        self.addCard(ModifierCard("Paralyzing Bite", 67, False, actions=["move-1", "attack+0.\n Consume Light->+1 attack, Stun"]))
        self.addCard(ModifierCard("Leaping Dive", 12, False, actions=["move+2. Jump", "attack-1", "Infuse Light"]))
        self.addCard(ModifierCard("Electric Pulse", 16, False, actions=["move-1", "attack+0. Range 2\n Infuse Light"]))
        self.addCard(ModifierCard("Hasty Assault", 5, False, actions=["move+1", "attack-1"]))
        self.shuffle()

class LivingBones(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Drain Life", 20, True, actions=["move-2", "attack+0", "Heal 2 self"]))
        self.addCard(ModifierCard("Nothing Special", 45, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Calculated Strike", 64, False, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Focused Stabs", 74, False, actions=["move+0", "attack+0. Target 1 enemy w/ all attacks"]))
        self.addCard(ModifierCard("Eternal Life", 12, True, actions=["Shield 1", "Heal 2 self"]))
        self.addCard(ModifierCard("Nothing Special", 45, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Hasty Assault", 25, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Power Slash", 81, False, actions=["move+2"]))
        self.shuffle()

class LivingDoom(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Chilling Aura", 70, False, actions=["move+0", "attack-1. 3 adj melee AOE", "Infuse Frost"]))
        self.addCard(ModifierCard("Fate of Darkness", 82, False, actions=["move-1", "attack+1.\n Consume Darkness->Disarm"]))
        self.addCard(ModifierCard("Arresting Advance", 32, False, actions=["move+1", "attack-1.\n Consume Frost->Immobilize"]))
        self.addCard(ModifierCard("Nothing Special", 57, False, actions=["move+0", "attack+0", "Consume Darkness"]))
        self.addCard(ModifierCard("Sunless Abyss", 11, False, actions=["Curse, Range 2", "Shield 1", "Retaliate 2, Range 2", "Infuse Frost and Darkness"]))
        self.addCard(ModifierCard("Hateful Spikes", 17, False, actions=["move+1", "Retaliate 2", "Infuse Darkness"]))
        self.addCard(ModifierCard("Pull of the Grave", 98, True, actions=["move+1", "attack-3. Bane"]))
        self.addCard(ModifierCard("Call for Souls", 78, True, actions=["Summon X normal Living Spirits\n Where X is the Living Doom's current HP divided by 5 (rounded down, Max 3)"]))

class LivingSpirit(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Sap Strength", 22, True, actions=["move-1", "attack-1. Range 3, Muddle"]))
        self.addCard(ModifierCard("Booming Scream", 33, True, actions=["move-1", "attack-1. Range 3, Target 3"]))
        self.addCard(ModifierCard("Nothing Special", 48, False, actions=["move+0", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Nothing Special", 48, False, actions=["move+0", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Coupled Chain", 61, False, actions=["attack+0. Range 3, Target 2"]))
        self.addCard(ModifierCard("Leech Warmth", 75, False, actions=["move-1", "attack+1. Range 2", "Heal 1 self", "Infuse Frost"]))
        self.addCard(ModifierCard("Angry Howl", 55, False, actions=["move+0", "Curse, Target 3, Range 2", "Infuse Frost"]))
        self.addCard(ModifierCard("Icy Glare", 67, False, actions=["move-1", "attack+0. Range 4\n Consume Frost->Stun"]))
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
        
class LurkerMindsnipper(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Psychic Shock", 6, True, actions=["Retaliate 3, Range 3\n Consume Darkness->Retaliate 2", "Muddle all, Range 3"]))
        self.addCard(ModifierCard("Beguiling Thoughts", 18, False, actions=["move+0", "attack-2. Range 2, Disarm"]))
        self.addCard(ModifierCard("Paralyze", 46, False, actions=["attack-1. Range 4\n Consume Darkness->Stun"]))
        self.addCard(ModifierCard("Hasty Assault", 10, False, actions=["move+2", "attack-1. Range 3", "Infuse Darkness"]))
        self.addCard(ModifierCard("Calculated Strike", 34, False, actions=["move-2", "attack+1. Range 3", "Infuse Darkness"]))
        self.addCard(ModifierCard("Consume All Hope", 22, False, actions=["move+0", "attack-1. Range 3, Curse", "Infuse Darkness"]))
        self.addCard(ModifierCard("Turn the Weak", 51, True, actions=["move+0", "attack-2. Range 3", "Control targets of attack in initiative order->\n Attack+3"]))
        self.addCard(ModifierCard("Instill Fear", 37, False, actions=["attack-1. +2 Targets, Range 3, Push 2"]))
        self.shuffle()
        
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
        
class LurkerWavethrower(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Powerful Claw", 60, False, actions=["mov-1", "attack+2"]))
        self.addCard(ModifierCard("Distant Wave", 51, False, actions=["Focus on farthest enemy within Range 6->", "attack+1. Range 6"]))
        self.addCard(ModifierCard("Tsunami", 29, False, actions=["move+1", "attack-1. Range2, Large Flower AoE"]))
        self.addCard(ModifierCard("Aid From Below", 98, True, actions=["Create a 1-hex water tile in adj empty hex", "Summon Lightning Eel in adj unnocupied water hex\n Normal Wavethrower summon normal, elite summon elite"]))
        self.addCard(ModifierCard("Aid From Below", 98, True, actions=["Create a 1-hex water tile in adj empty hex", "Summon Lightning Eel in adj unnocupied water hex\n Normal Wavethrower summon normal, elite summon elite"]))
        self.addCard(ModifierCard("Crushing Crest", 36, False, actions=["move+1", "attack-1. 3 Hex melee adjacent AoE"]))
        self.addCard(ModifierCard("Twin Claws", 48, False, actions=["move+0", "attack+0. 2 Hex melee adj AoE"]))
        self.addCard(ModifierCard("Massive Shell", 40, False, actions=["move+0", "attack+0. Range 3, small triangle AoE"]))
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
        
class Ooze(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 36, False, actions=["move+1", "attack-1. Range 3", "Infuse Earth"]))
        self.addCard(ModifierCard("Nothing Special", 57, False, actions=["move+0", "attack+0. Range 3"]))
        self.addCard(ModifierCard("Toxic Explosion", 59, False, actions=["move+0. Target 2, Range 3, Poison\n Consume Earth->+1 Target"]))
        self.addCard(ModifierCard("Plasma Ward", 85, False, actions=["Push 1, Target all, Range 1, Poison", "attack+1. Range 2"]))
        self.addCard(ModifierCard("Calculated Strike", 66, False, actions=["move-1", "attack+1. Range 4", "Infuse Darkness"]))
        self.addCard(ModifierCard("Split", 94, True, actions=["Ooze suffers 2 damage", "Summon one normal Ooze w/ HP equal to Ooze's current HP (limited by normal Ooze max HP)"]))
        self.addCard(ModifierCard("Split", 94, True, actions=["Ooze suffers 2 damage", "Summon one normal Ooze w/ HP equal to Ooze's current HP (limited by normal Ooze max HP)"]))
        self.addCard(ModifierCard("Feed", 66, False, actions=["move-1", "Loot 1", "Heal 2 self\n Consume Darkness->+1 Heal"]))
        self.shuffle()

class PiranhaPig(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Schooling", 40, True, actions=["move+0", "attack+0. Add +1 if target adj to any PiranhaPig allies"]))
        self.addCard(ModifierCard("Bloodthirst", 38, False, actions=["move+1", "attack-1. Add +2 if target has Wound"]))
        self.addCard(ModifierCard("Easy Prey", 54, False, actions=["move-1", "attack+1. Add +1 if target occupying hex with a water tile"]))
        self.addCard(ModifierCard("Feast", 26, False, actions=["attack+0", "Heal X, X is dmg suffered by target of attack"]))
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

class RendingDrake(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Hasty Assault", 12, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Swift Claws", 13, True, actions=["attack-1", "move-1", "attack-1"]))
        self.addCard(ModifierCard("Nothing Special", 25, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Calculated Strike", 39, False, actions=["move-1", "attack+1"]))
        self.addCard(ModifierCard("Venom Glands", 54, False, actions=["move-2", "attack-1. Target 2, Range 3, Poison"]))
        self.addCard(ModifierCard("Dangerous Fury", 59, False, actions=["move-2", "attack+1. Range 2"]))
        self.addCard(ModifierCard("Unending Frenzy", 72, True, actions=["attack-1", "attack-1", "attack-2"]))
        self.addCard(ModifierCard("Empowering Rest", 6, False, actions=["Shield 2", "Heal 2 self, Strengthen"]))
        self.shuffle()

class RoboticBoltshooter(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Calculated Shot", 83, False, actions=["move-1", "attack+1. Range 5"]))
        self.addCard(ModifierCard("Safety Valve", 22, True, actions=["move-1", "attack-1. Range 4", "Shield 2"]))
        self.addCard(ModifierCard("Sharpshooter", 44, False, actions=["move+1", "attack-1. Range 5, Pierce 2"]))
        self.addCard(ModifierCard("Retracted Assault", 48, False, actions=["move-1", "attack+0. Range 4", "Shield 1"]))
        self.addCard(ModifierCard("Nothing Special", 57, False, actions=["move+0", "attack+0. Range 5"]))
        self.addCard(ModifierCard("Ballista Bolt", 91, False, actions=["attack+2. -1 Target, Range 4"]))
        self.addCard(ModifierCard("Focus Fire", 78, False, actions=["move+0", "attack-1. Target 1 enemy w/ all attack"]))
        self.addCard(ModifierCard("Repair Drones", 16, True, actions=["Shield 1", "Heal 3 self"]))
        self.shuffle()

class RuinedMachine(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Calculated Strike", 85, False, actions=["move+1","attack+1"]))
        self.addCard(ModifierCard("Hasty Assault", 41, False, actions=["move+1", "attack-1"]))
        self.addCard(ModifierCard("Signal Jam", 56, True, actions=["move+0", "Muddle All, Range 2\n Ruined Machine Suffers 1"]))
        self.addCard(ModifierCard("Nothing Special", 63, False, actions=["move+0", "attack+0"]))
        self.addCard(ModifierCard("Devastating Tackle", 42, False, actions=["attack+2. Immobilize", "If Attack performed, Suffer 1 self"]))
        self.addCard(ModifierCard("Latch On", 31, False, actions=["move+1", "Poison, Immobilize, Range 1"]))
        self.addCard(ModifierCard("Self-Destruct", 93, True, actions=["move+0", "attack+0", "If Attack performed all adj enemies suffer trap damage\n Ruined machine dies."]))
        self.addCard(ModifierCard("Fuel Leak", 29, False, actions=["move+1", "If Move performed, Suffer 1 self", "attack+0"]))
        self.shuffle()
        
class SavvasIcestorm(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Repulsive Torrent", 70, False, actions=["Push 2, Target all, Range 1\n Consume Wind->+2 Push", "attack+1. Range 5"]))
        self.addCard(ModifierCard("Call of the Wind", 98, False, actions=["Summon one normal Wind Demon", "Infuse Wind"]))
        self.addCard(ModifierCard("Call of the Frost", 98, False, actions=["Summon one normal Frost Demon"]))
        self.addCard(ModifierCard("Hardened Frost", 19, False, actions=["move+0", "attack-1. Range 3", "Grant all allies within Range 2, and self, Shield 1", "Infuse Frost"]))
        self.addCard(ModifierCard("Freezing Winds", 14, False, actions=["attack+0. Range 4\n Consume Frost->+2 attack, Immobilize", "Retaliate 2", "Infuse Wind"]))
        # TODO Frozen Shell attack on consume wind text formatting
        self.addCard(ModifierCard("Frozen Shell", 14, False, actions=["Shield 4", "Heal 2 self, Range 3\n Consume Earth->+3 Heal", "Consume Wind->","attack-1. Range 3"]))
        self.addCard(ModifierCard("Forceful Gust", 47, True, actions=["Disarm all, Range 1", "move+0", "attack-1. Range 4", "Infuse Wind"]))
        self.addCard(ModifierCard("Cone of Cold", 35, True, actions=["move-1", "attack-1. 2 Range Cone AoE", "Infuse Frost"]))
        self.shuffle()

class SavvasLavaflow(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Call of the Flame", 97, False, actions=["Summon one normal Flame Demon", "Infuse Fire"]))
        self.addCard(ModifierCard("Call of the Earth", 97, False, actions=["Summon one normal Earth Demon", "Infuse Earth"]))
        self.addCard(ModifierCard("Circle of Fire", 22, False, actions=["move+1", "attack-1. Target all adj enemies", "Consume Fire->Retaliate 3"]))
        self.addCard(ModifierCard("Rock Bomb", 68, True, actions=["move-1", "attack+1. Range 3, All allies and enemies adj to target suffer 2 damage", "Infuse Earth"]))
        self.addCard(ModifierCard("Stone Spikes", 41, False, actions=["move+0", "attack-1. 3 Hex melee Line AoE\n Consume Earth->+2 attack, Immobilize"]))
        self.addCard(ModifierCard("Flowing Magma", 51, False, actions=["All enemies within Range 5 suffer 2 damage", "Consume Fire->Wound all, Range 5", "Consume Earth->Disarm all, Range 4"]))
        self.addCard(ModifierCard("Strength of the Mountain", 31, False, actions=["Heal 4, Range 3\n Consume Earth->+2 Targets"]))
        self.addCard(ModifierCard("Fire Bolts", 68, True, actions=["move-1","attack-1. Target 2, Range 3", "Infuse Fire"]))
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

class SunDemon(Deck):
    def __init__(self):
        super().__init__()
        self.addCard(ModifierCard("Ray of Warmth", 17, True, actions=["Heal 3, Range 3\n Consume Light->Target all"]))
        self.addCard(ModifierCard("Brilliant Aura", 36, False, actions=["move+0", "attack+0. Target all adj enemies", "Infuse"]))
        self.addCard(ModifierCard("Brilliant Aura", 36, False, actions=["move+0", "attack+0. Target all adj enemies", "Infuse"]))
        self.addCard(ModifierCard("Star Strike", 68, False, actions=["move+0", "attack+1", "Infuse Light"]))
        self.addCard(ModifierCard("Vicious Opportunity", 73, True, actions=["move-1", "attack+1", "Consume Light->Heal 3 self"]))
        self.addCard(ModifierCard("Supernova", 95, False, actions=["move-1", "attack+0. Range 3\n Consume Light->Target all"]))
        self.addCard(ModifierCard("Glowing Sweep", 88, False, actions=["move-1", "attack-1. Target all adj enemies", "Consume Darkness->Muddle self"]))
        self.addCard(ModifierCard("Shining Orb", 50, False, actions=["move+0", "attack+0. Range 3\n Consume any->Infuse Light"]))
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
    

    

    

    