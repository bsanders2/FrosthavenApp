# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:21:16 2023

@author: blake
"""

from copy import copy

class Monster:
    def __init__(self, level=0, name='Default', elite=0, deck_name='Default'):
        self.level = level
        self.name = name
        self.deck_name = deck_name
        self.standee = 0
        self.elite = elite
        self.health = 0
        self.move = 0
        self.attack = 0
        self.innate = ""
        
    def __repr__(self):
        return "{}:{}".format(self.getName(), self.standee)
        
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
    deck_name = "Archer"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])
        
class AlgoxGuard(Monster):
    properties = {0:[[6,2,3],[10,2,4]], 1:[[7,3,3],[12,3,4]]}
    name = "AlgoxGuard"
    deck_name = "Guard"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])
        
class AlgoxPriest(Monster):
    properties = {0:[[5,2,2],[7,3,3]], 1:[[6,2,2],[7,3,3]], 2:[[7,2,3],[9,3,3]]}
    name = "AlgoxPriest"
    deck_name = "Priest"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
        
class AlgoxScout(Monster):
    properties = {0:[[7,3,2],[10,4,3]], 1:[[8,4,2],[12,4,3]], 2:[[11,4,2],[13,5,4]]}  
    name = "AlgoxScout"
    deck_name = "Scout"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Elites have Impair
        self.updateProperties(self.properties[level][elite], innate)

class BurrowingBlade(Monster):
    properties = {0:[[4,2,2],[5,3,3]], 1:[[4,3,2],[5,4,3]], 2:[[5,3,3],[6,4,4]], 3:[[7,3,3],[7,4,5]]}  
    name = "BurrowingBlade"
    deck_name = "BurrowingBlade"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" 
        self.updateProperties(self.properties[level][elite], innate)


class DeepTerror(Monster):
    properties = {0:[[3,None,2],[5,None,3]], 1:[[4,None,2],[6,None,3]], 2:[[4,None,3],[7,None,4]]}  
    name = "DeepTerror"
    deck_name = "DeepTerror"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        # if level > 0 and elite:
        #     innate = "Impair"
        self.updateProperties(self.properties[level][elite], innate)

class FlamingBladespinner(Monster):
    properties = {0:[[6,2,2],[8,2,3]], 1:[[6,2,2],[10,2,3]], 2:[[7,2,3],[13,2,3]], 3:[[8,3,3],[15,2,4]]}
    name = "FlamingBladespinner"
    deck_name = "FlamingBladespinner"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        if elite:
            innate += "Retaliate 3"
        else:
            innate += "Retaliate 2"
        self.updateProperties(self.properties[level][elite], innate)
        
class ForestImp(Monster):
    properties = {0:[[1,3,1],[4,3,1]], 1:[[2,3,1],[5,3,2]], 2:[[2,3,2],[6,3,2]]}
    name = "ForestImp"
    deck_name = "Imp"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        if level < 4:
            innate = "Shield 1"
        else:
            innate = "Shield 2"
        if level > 1 and elite:
            innate += ", Curse"
        self.updateProperties(self.properties[level][elite], innate)
        
class FrozenCorpse(Monster):
    properties = {0: [[7,1,2],[10,2,2]], 1: [[7,1,2],[10,2,2]]}  
    name = "FrozenCorpse"
    deck_name = "FrozenCorpse"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        if level > 1:
            innate += "Shield 1"
        if level > 0 and elite:
            innate += ", Retaliate 1"
        self.updateProperties(self.properties[level][elite], innate)
        
class HarrowerInfester(Monster):
    properties = {0:[[6,2,2],[12,2,2]], 1:[[7,2,2],[12,3,2]], 2:[[8,2,2],[14,3,3]]}
    name = "HarrowerInfester"
    deck_name = "HarrowerInfester"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        # if level > 1:
        #     innate += "Shield 1"
        # if level > 0 and elite:
        #     innate += ", Retaliate 1"
        self.updateProperties(self.properties[level][elite], innate)

class Hound(Monster):
    properties = {0:[[4,3,2],[6,5,2]], 1:[[4,4,2],[6,4,2]], 2:[[5,4,2],[7,5,3]], 3:[[8,4,2],[8,5,4]]}
    name = "Hound"
    deck_name = "Hound"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # retaliate
        self.updateProperties(self.properties[level][elite], innate)
        
class IceWraith(Monster):
    properties = {0: [[7,2,2],[7,4,3]], 1: [[8,2,2],[8,4,3]], 2:[[10,3,2],[10,5,3]]}
    name = "IceWraith"
    deck_name = "IceWraith"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        if elite and level > 0:
            innate += "Retaliate 2, rng 2"
        if not elite:
            if level > 0:
                innate += ", Shield 2"
            else:
                innate += ", Shield 1"
        self.updateProperties(self.properties[level][elite], innate)

class LurkerClawcrusher(Monster):
    properties = {0:[[7,2,2],[10,2,3]], 1:[[8,2,2], [10,2,3]], 2:[[10,3,2],[13,3,3]], 3:[[13,3,2],[14,3,4]]}
    name = "LurkerClawcrusher"
    deck_name = "LurkerClawcrusher"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Target 2, Shield varies, Elites have impair
        self.updateProperties(self.properties[level][elite], innate)
        
class LurkerMindsnipper(Monster):
    properties = {0:[[5,2,2],[7,2,3]], 1:[[6,2,2],[7,3,3]]} 
    name = "LurkerMindsnipper"
    deck_name = "LurkerMindsnipper"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "Target 2"
        if level > 0 and not elite:
            innate += ", Pierce 2"
        if level > 0 and elite:
            innate += ", Pierce 3, Muddle"
        self.updateProperties(self.properties[level][elite], innate)
        
class LurkerSoldier(Monster):
    properties = {0:[[5,2,2],[7,2,3]], 1:[[7,2,2],[9,2,3]], 2:[[9,3,2],[11,3,3]], 3:[[10,3,3],[13,3,4]]}
    name = "LurkerSoldier"
    deck_name = "LurkerSoldier"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Pierce, Target 2, Elites have Shield
        self.updateProperties(self.properties[level][elite], innate)
        
class NightDemon(Monster):
    properties = {0:[[3,3,3],[5,4,4]], 1:[[5,3,3],[8,4,4]], 2:[[6,3,4],[11,4,4]]}  
    name = "NightDemon"
    deck_name = "NightDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Attackers gain disadvantage
        self.updateProperties(self.properties[level][elite], innate)

class PiranhaPig(Monster):
    properties = {0:[[4,2,2],[7,2,3]], 1:[[5,3,2],[7,3,3]], 2:[[6,3,3],[9,4,3]], 3:[[8,3,3],[11,4,4]]}  
    name = "PiranhaPig"
    deck_name = "PiranhaPig"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #  Elites have Wound
        self.updateProperties(self.properties[level][elite], innate)
        
class PolarBear(Monster):
    properties = {0:[[6,2,3],[10,2,4]], 1:[[8,2,3],[12,2,4]], 2:[[10,2,3],[14,3,4]], 3:[[10,3,3],[16,3,5]]}  
    name = "PolarBear"
    deck_name = "PolarBear"
    num_standees = 4
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # immune to immobilize, stun. Some have innate wound.
        self.updateProperties(self.properties[level][elite], innate)

class RuinedMachine(Monster):
    properties = {0: [[3,1,1],[5,1,2]], 1:[[5,1,1],[8,1,2]], 2:[[6,2,1],[9,2,2]], 3:[[6,2,2],[10,2,3]]}  
    name = "RuinedMachine"
    deck_name = "RuinedMachine"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #Immune to poison
        self.updateProperties(self.properties[level][elite], innate)
    
class SnowImp(Monster):
    properties = {0:[[2,2,1],[4,2,2]], 1:[[2,2,1],[4,2,2]], 2:[[3,2,1],[5,3,2]], 3:[[3,2,2],[7,3,2]]}
    name = "SnowImp"
    deck_name = "Imp"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
        
class ShrikeFiend(Monster):
    properties = {0:[[6,1,2],[8,2,3]], 1:[[8,1,2],[10,2,3]], 2:[[9,1,3],[12,2,4]], 3:[[10,2,3],[16,2,4]]}
    name = "ShrikeFiend"
    deck_name = "ShrikeFiend"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)

class SpittingDrake(Monster):
    properties = {0:[[4,3,3],[7,3,4]], 1:[[5,3,3],[9,3,4]], 2:[[7,3,3],[10,3,5]], 3:[[8,3,4],[13,3,5]]}
    name = "SpittingDrake"
    deck_name = "SpittingDrake"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Muddle 
        self.updateProperties(self.properties[level][elite], innate)

class SteelAutomaton(Monster):
    properties = {0:[[9,1,3],[10,2,4]], 1:[[9,2,3],[12,2,4]], 2:[[12,2,3],[14,2,5]], 3:[[14,2,4],[17,3,5]]}
    name = "SteelAutomaton"
    deck_name = "SteelAutomaton"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Immune to poison and disarm. Shield varies
        self.updateProperties(self.properties[level][elite], innate)
        
class WindDemon(Monster):
    properties = {0:[[3,3,2],[5,4,3]], 1:[[3,3,2],[5,3,3]], 2:[[4,4,2],[7,4,3]], 3:[[5,4,3],[8,4,4]]}
    name = "WindDemon"
    deck_name = "WindDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
    
        
        
        
        
        
        
        