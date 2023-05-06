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

class AbaelHerder(Monster):
    properties = {
        0: [[4,3,2],[6,3,3]], 1:[[6,3,2],[9,3,3]], 2:[[8,3,2],[11,4,3]], 3:[[9,3,3],[13,4,4]], \
        4:[[11,4,3],[17,4,4]], 5: [[14,4,3],[20,4,5]], 6:[[18,4,4],[29,5,5]], 7:[[24,4,4],[36,5,6]] \
    }
    name = "AbaelHerder"
    deck_name = "AbaelHerder"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])   

class AbaelScout(Monster):
    properties = {
        0: [[2,3,3],[5,4,3]], 1:[[3,3,3],[5,4,4]], 2:[[4,4,3],[7,4,4]], 3:[[4,4,4],[9,5,4]], \
        4:[[5,4,4],[10,5,5]], 5:[[7,4,4],[13,5,5]], 6:[[10,4,5],[17,5,6]], 7:[[14,4,5],[23,5,6]] \
    }
    name = "AbaelScout"
    deck_name = "AbaelScout"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])   

class AlgoxArcher(Monster):
    properties = {
        0: [[4,1,3],[6,2,4]], 1:[[5,2,3],[8,2,4]], 2:[[7,2,3],[11,2,4]], 3:[[7,2,4],[12,2,5]], \
        4:[[10,2,4],[16,2,5]], 5:[[13,2,4],[18,2,6]], 6:[[19,2,4],[28,2,6]], 7:[[22,2,5],[33,2,7]] \
    }
    name = "AlgoxArcher"
    deck_name = "Archer"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])
        
class AlgoxGuard(Monster):
    properties = {
        0: [[6,2,3],[10,2,4]], 1:[[7,3,3],[12,3,4]], 2:[[10,3,3],[15,3,5]], 3:[[12,3,4],[19,4,5]], \
        4:[[15,4,4],[22,4,6]], 5:[[19,4,4],[27,5,6]], 6:[[25,4,5],[37,5,7]], 7:[[33,5,5],[47,6,7]] \
    }
    name = "AlgoxGuard"
    deck_name = "Guard"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])

class AlgoxIcespeaker(Monster):
    properties = {
        0: [[6,2,3],[8,2,4]], 1:[[8,2,3],[8,2,4]], 2:[[10,2,3],[10,3,4]], 3:[[12,3,3],[12,3,5]], \
        4:[[14,3,4],[15,4,5]], 5:[[15,3,4],[18,4,6]], 6:[[20,3,5],[26,4,6]], 7:[[27,4,5],[35,4,6]] \
    }
    name = "AlgoxIcespeaker"
    deck_name = "AlgoxIcespeaker"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        self.updateProperties(self.properties[level][elite])
        
class AlgoxPriest(Monster):
    properties = {
        0:[[5,2,2],[7,3,3]], 1:[[6,2,2],[7,3,3]], 2:[[7,2,3],[9,3,3]], 3:[[9,2,3],[12,3,3]], \
        4:[[12,2,3],[14,3,4]], 5:[[15,2,3],[19,3,4]], 6:[[20,2,4],[25,3,5]], 7:[[27,2,4],[34,3,5]] \
    }
    name = "AlgoxPriest"
    deck_name = "Priest"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)

class AlgoxSnowspeaker(Monster):
    properties = {
        0:[[5,2,2],[7,3,3]], 1:[[6,2,2],[7,3,3]], 2:[[7,2,3],[9,3,3]], 3:[[9,2,3],[12,3,3]], \
        4:[[12,2,3],[14,3,4]], 5:[[15,2,3],[19,3,4]], 6:[[20,2,4],[25,3,5]], 7:[[27,2,4],[34,3,5]] \
    }
    name = "AlgoxSnowspeaker"
    deck_name = "AlgoxSnowspeaker"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Elites have Impair
        self.updateProperties(self.properties[level][elite], innate)

class AlgoxScout(Monster):
    properties = {}
    properties = {
        0:[[7,3,2],[10,4,3]], 1:[[8,4,2],[12,4,3]], 2:[[11,4,2],[13,5,4]], 3:[[12,4,3],[17,5,4]], \
        4:[[15,4,3],[22,5,4]], 5:[[18,5,3],[26,5,5]], 6:[[24,5,4],[32,6,6]], 7:[[33,5,4],[40,6,7]] \
    }  
    name = "AlgoxScout"
    deck_name = "Scout"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Elites have Impair
        self.updateProperties(self.properties[level][elite], innate)

class AncientArtillery(Monster):
    properties = {
        0:[[4,0,2],[7,0,3]], 1:[[6,0,2],[9,0,3]], 2:[[8,0,2],[12,0,3]], 3:[[9,0,4],[14,0,4]], \
        4:[[12,0,3],[16,0,5]], 5:[[15,0,3],[21,0,5]], 6:[[18,0,4],[26,0,6]], 7:[[21,0,5],[34,0,7]] \
    }  
    name = "AncientArtillery"
    deck_name = "AncientArtillery"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Immune to muddle
        self.updateProperties(self.properties[level][elite], innate)

class BlackImp(Monster):
    properties = {
        0:[[3,1,1],[3,1,2]], 1:[[3,1,1],[5,1,2]], 2:[[4,1,1],[7,1,2]], 3:[[4,1,2],[7,1,2]], \
        4:[[5,1,2],[7,1,3]], 5:[[7,1,2],[9,1,3]], 6:[[9,1,3],[12,1,4]], 7:[[13,1,3],[18,1,4]] \
    }  
    name = "BlackImp"
    deck_name = "BlackImp"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Immune to muddle
        self.updateProperties(self.properties[level][elite], innate)

class BurrowingBlade(Monster):
    properties = {
        0:[[1,2,2],[5,3,3]], 1:[[4,3,2],[5,4,3]], 2:[[5,3,3],[6,4,4]], 3:[[7,3,3],[7,4,5]], \
        4:[[7,3,3],[9,4,5]], 5:[[8,3,4],[11,5,5]], 6:[[11,4,4],[15,5,6]], 7:[[13,4,5],[19,5,7]] \
    }  
    name = "BurrowingBlade"
    deck_name = "BurrowingBlade"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" 
        self.updateProperties(self.properties[level][elite], innate)

class ChaosDemon(Monster):
    properties = {0:[[7,3,2],[10,4,3]], 1:[[8,3,3],[12,4,4]], 2:[[11,3,3],[14,4,5]], 3:[[12,3,4],[18,5,5]], \
                  4:[[14,4,4],[21,5,6]], 5:[[16,4,5],[26,5,6]], 6:[[20,4,6],[33,5,8]], 7:[[25,4,7],[39,6,9]]}
    name = "ChaosDemon"
    deck_name = "ChaosDemon"
    num_standees = 1
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Muddle
        self.updateProperties(self.properties[level][elite], innate)

class CityGuard(Monster):
    properties = {
        0:[[5,2,2],[6,2,3]], 1:[[5,2,2],[6,2,3]], 2:[[7,2,2],[9,2,3]], 3:[[8,2,3],[9,2,4]], \
        4:[[9,3,3],[10,3,4]], 5:[[10,3,3],[10,3,4]], 6:[[13,3,4],[15,3,4]], 7:[[17,3,4],[20,3,5]] \
    }  
    name = "CityGuard"
    deck_name = "Guard"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Muddle
        self.updateProperties(self.properties[level][elite], innate)

class DeepTerror(Monster):
    properties = {
        0:[[3,0,5],[5,0,3]], 1:[[4,0,2],[6,0,3]], 2:[[4,0,3],[7,0,4]], 3:[[5,0,3],[8,0,4]], \
        4:[[7,0,3],[9,0,5]], 5:[[7,0,4],[11,0,5]], 6:[[9,0,4],[13,0,6]], 7:[[9,0,5],[16,0,6]] \
    }  
    name = "DeepTerror"
    deck_name = "DeepTerror"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        # if level > 0 and elite:
        #     innate = "Impair"
        self.updateProperties(self.properties[level][elite], innate)

class EarthDemon(Monster):
    properties = {
        0:[[7,1,3],[10,2,4]], 1:[[9,1,3],[13,2,4]], 2:[[12,1,3],[18,2,4]], 3:[[13,2,3],[20,2,4]], \
        4:[[15,2,4],[21,3,5]], 5:[[17,2,4],[25,3,5]], 6:[[21,3,4],[32,3,6]], 7:[[25,3,5],[42,3,7]] \
    }  
    name = "EarthDemon"
    deck_name = "EarthDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # 
        self.updateProperties(self.properties[level][elite], innate)

class FlameDemon(Monster):
    properties = {
        0:[[2,3,2],[3,3,2]], 1:[[2,3,2],[3,3,2]], 2:[[3,3,3],[4,3,3]], 3:[[3,3,3],[5,3,3]], \
        4:[[3,4,3],[5,4,4]], 5:[[4,4,3],[6,4,4]], 6:[[4,4,4],[7,4,5]], 7:[[6,4,4],[9,4,6]] \
    }  
    name = "FlameDemon"
    deck_name = "FlameDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # 
        self.updateProperties(self.properties[level][elite], innate)

class FlamingBladespinner(Monster):
    properties = {
        0:[[6,2,2],[8,2,3]], 1:[[6,2,2],[10,2,3]], 2:[[7,2,3],[13,2,3]], 3:[[8,3,3],[15,2,4]], \
        4:[[11,3,3],[15,3,4]], 5:[[13,3,4],[18,3,5]], 6:[[19,3,4],[24,3,5]], 7:[[22,4,4],[32,4,5]] \
    }  
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
    properties = {
        0:[[1,3,1],[4,3,1]], 1:[[2,3,1],[5,3,2]], 2:[[2,3,2],[6,3,2]], 3:[[3,4,2],[7,4,2]], \
        4:[[3,4,2],[7,4,2]], 5:[[4,4,2],[8,4,3]], 6:[[5,4,3],[10,4,4]], 7:[[8,4,3],[14,4,4]] \
    }  
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

class FrostDemon(Monster):
    properties = {
        0:[[5,2,3],[10,3,1]], 1:[[6,2,3],[10,3,3]], 2:[[7,3,3],[12,4,4]], 3:[[8,3,4],[14,4,4]], \
        4:[[11,3,4],[19,4,4]], 5:[[13,3,4],[22,4,5]], 6:[[18,3,5],[29,4,6]], 7:[[25,3,5],[40,4,7]] \
    }  
    name = "FrostDemon"
    deck_name = "FrostDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
        
class FrozenCorpse(Monster):
    properties = {0: [[7,1,2],[10,2,2]], 1: [[7,1,2],[10,2,2]], 2:[[9,1,2],[11,2,3]], 3:[[10,2,2],[14,2,3]], \
        4:[[12,2,3],[17,2,4]], 5:[[15,2,3],[20,3,4]], 6:[[17,2,4],[24,3,5]], 7:[[23,3,5],[31,4,6]]}  
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
    properties = {0:[[6,2,2],[12,2,2]], 1:[[7,2,2],[12,3,2]], 2:[[8,2,2],[14,3,3]], 3:[[10,2,3],[17,3,3]], \
        4:[[12,3,3],[19,3,4]], 5:[[12,3,4],[21,3,5]], 6:[[15,3,5],[27,3,6]], 7:[[18,3,5],[32,4,6]]}  
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
    properties = {0:[[4,3,2],[6,5,2]], 1:[[4,4,2],[6,4,2]], 2:[[5,4,2],[7,5,3]], 3:[[8,4,2],[8,5,4]], \
        4:[[9,4,3],[11,5,4]], 5:[[10,4,3],[13,5,4]], 6:[[14,5,3],[17,6,5]], 7:[[17,5,4],[23,6,6]]}  
    name = "Hound"
    deck_name = "Hound"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # retaliate
        self.updateProperties(self.properties[level][elite], innate)
        
class IceWraith(Monster):
    properties = {0: [[7,2,2],[7,4,3]], 1: [[8,2,2],[8,4,3]], 2:[[10,3,2],[10,5,3]], 3:[[10,3,3],[10,5,4]], \
        4:[[12,3,3],[12,5,4]], 5:[[16,3,3],[16,5,5]], 6:[[21,3,4],[21,5,5]], 7:[[27,3,5],[27,5,6]]} 
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

class LightningEel(Monster):
    properties = {0: [[1,2,2],[3,3,2]], 1: [[2,2,2],[3,3,3]], 2:[[3,3,2],[5,3,3]], 3:[[4,3,2],[6,4,3]], \
        4:[[5,3,3],[7,4,4]], 5:[[6,3,3],[9,4,4]], 6:[[9,4,3],[13,4,5]], 7:[[11,4,4],[17,4,6]]} 
    name = "LightningEel"
    deck_name = "LightningEel"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # treats water hexes as corridors and non-water as obstacles
        self.updateProperties(self.properties[level][elite], innate)

class LivingBones(Monster):
    properties = {0: [[5,2,1],[6,4,2]], 1: [[5,3,1],[6,4,2]], 2:[[5,3,2],[7,4,3]], 3:[[7,3,2],[9,4,3]], \
        4:[[7,3,3],[10,4,4]], 5:[[9,3,3],[13,4,4]], 6:[[12,4,3],[18,5,4]], 7:[[15,4,4],[21,6,5]]} 
    name = "LivingBones"
    deck_name = "LivingBones"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # # target 2 and shield
        self.updateProperties(self.properties[level][elite], innate)

class LivingDoom(Monster):
    properties = {0: [[8,2,3],[10,2,4]], 1: [[8,2,3],[10,3,4]], 2:[[9,2,4],[11,3,5]], 3:[[9,2,4],[14,4,5]], \
        4:[[11,3,4],[18,4,5]], 5:[[14,3,4],[20,4,6]], 6:[[18,3,5],[27,4,7]], 7:[[24,4,5],[30,4,7]]} 
    name = "LivingDoom"
    deck_name = "LivingDoom"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # # target 2 and shield
        self.updateProperties(self.properties[level][elite], innate)

class LivingSpirit(Monster):
    properties = {0: [[2,2,2],[3,3,3]], 1: [[2,2,2],[3,3,3]], 2:[[2,2,3],[3,3,4]], 3:[[3,3,3],[4,4,4]], \
        4:[[3,3,3],[4,4,4]], 5:[[4,3,3],[5,4,5]], 6:[[6,3,4],[8,4,5]], 7:[[7,4,5],[10,4,6]]} 
    name = "LivingSpirit"
    deck_name = "LivingSpirit"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # # target 2 and shield
        self.updateProperties(self.properties[level][elite], innate)

class LurkerClawcrusher(Monster):
    properties = {0:[[7,2,2],[10,2,3]], 1:[[8,2,2], [10,2,3]], 2:[[10,3,2],[13,3,3]], 3:[[13,3,2],[14,3,4]], \
        4:[[13,3,2],[18,3,4]], 5:[[15,3,3],[21,3,5]], 6:[[21,3,4],[22,3,6]], 7:[[23,3,5],[29,3,7]]} 
    name = "LurkerClawcrusher"
    deck_name = "LurkerClawcrusher"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Target 2, Shield varies, Elites have impair
        self.updateProperties(self.properties[level][elite], innate)
        
class LurkerMindsnipper(Monster):
    properties = {0:[[5,2,2],[7,2,3]], 1:[[6,2,2], [7,3,3]], 2:[[6,2,3],[8,3,4]], 3:[[7,3,3],[11,3,4]], \
        4:[[9,3,3],[13,4,4]], 5:[[12,3,3],[15,4,5]], 6:[[15,3,4],[22,5,5]], 7:[[20,4,4],[27,5,6]]} 
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
    properties = {0:[[5,2,2],[7,2,3]], 1:[[7,2,2], [9,2,3]], 2:[[9,3,2],[11,3,3]], 3:[[10,3,3],[13,3,4]], \
        4:[[10,3,3],[13,3,4]], 5:[[11,3,4],[15,3,5]], 6:[[16,4,4],[19,4,6]], 7:[[20,4,5],[27,4,7]]} 
    name = "LurkerSoldier"
    deck_name = "LurkerSoldier"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Pierce, Target 2, Elites have Shield
        self.updateProperties(self.properties[level][elite], innate)

class LurkerWavethrower(Monster):
    properties = {0:[[4,1,1],[6,1,2]], 1:[[6,1,1], [7,1,2]], 2:[[8,1,1],[9,2,2]], 3:[[10,2,1],[11,2,2]], \
        4:[[11,2,2],[13,2,3]], 5:[[14,2,2],[16,3,3]], 6:[[17,3,2],[21,3,3]], 7:[[20,3,3],[26,3,4]]} 
    name = "LurkerWavethrower"
    deck_name = "LurkerWavethrower"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" 
        self.updateProperties(self.properties[level][elite], innate)
        
class NightDemon(Monster):
    properties = {0:[[3,3,3],[5,4,4]], 1:[[5,3,3], [8,4,4]], 2:[[6,3,4],[11,4,4]], 3:[[7,4,4],[13,4,5]], \
        4:[[8,4,4],[15,5,5]], 5:[[11,4,5],[17,5,6]], 6:[[16,4,5],[23,5,7]], 7:[[20,4,6],[30,5,8]]}  
    name = "NightDemon"
    deck_name = "NightDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Attackers gain disadvantage
        self.updateProperties(self.properties[level][elite], innate)

class Ooze(Monster):
    properties = {0:[[4,1,2],[8,1,2]], 1:[[5,1,2], [9,1,2]], 2:[[7,1,2],[11,1,3]], 3:[[8,1,3],[11,2,3]], \
        4:[[9,2,3],[12,2,4]], 5:[[10,2,3],[15,3,4]], 6:[[13,2,4],[21,3,4]], 7:[[17,2,4],[27,3,5]]}  
    name = "Ooze"
    deck_name = "Ooze"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Shield, poison
        self.updateProperties(self.properties[level][elite], innate)

class PiranhaPig(Monster):
    properties = {0:[[4,2,2],[7,2,3]], 1:[[5,3,2], [7,3,3]], 2:[[6,3,3],[9,4,3]], 3:[[8,3,3],[11,4,4]], \
        4:[[9,3,3],[15,4,4]], 5:[[11,4,3],[19,5,4]], 6:[[15,4,4],[25,5,5]], 7:[[21,4,4],[33,5,6]]}  
    name = "PiranhaPig"
    deck_name = "PiranhaPig"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #  Elites have Wound
        self.updateProperties(self.properties[level][elite], innate)
        
class PolarBear(Monster):
    properties = {0:[[6,2,3],[10,2,4]], 1:[[8,2,3], [12,2,4]], 2:[[10,2,3],[14,3,4]], 3:[[10,3,3],[16,3,5]], \
        4:[[12,3,4],[20,4,5]], 5:[[16,3,4],[24,4,6]], 6:[[23,4,4],[36,4,6]], 7:[[29,4,5],[44,4,7]]}  
    name = "PolarBear"
    deck_name = "PolarBear"
    num_standees = 4
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # immune to immobilize, stun. Some have innate wound.
        self.updateProperties(self.properties[level][elite], innate)

class RendingDrake(Monster):
    properties = {0:[[5,3,3],[7,4,4]], 1:[[6,3,3], [7,4,5]], 2:[[7,4,3],[9,5,5]], 3:[[7,4,4],[10,5,6]], \
        4:[[9,4,4],[12,6,6]], 5:[[10,4,5],[15,6,6]], 6:[[14,5,5],[19,6,7]], 7:[[18,5,6],[24,6,8]]}  
    name = "RendingDrake"
    deck_name = "RendingDrake"
    num_standees = 4
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # immune to immobilize, stun. Some have innate wound.
        self.updateProperties(self.properties[level][elite], innate)

class RoboticBoltshooter(Monster):
    properties = {0:[[4,1,1],[7,1,1]], 1:[[4,1,2], [7,1,2]], 2:[[6,1,2],[9,1,2]], 3:[[6,1,2],[10,1,2]], \
        4:[[6,1,3],[11,1,3]], 5:[[8,2,3],[14,2,3]], 6:[[10,2,4],[17,2,4]], 7:[[13,2,4],[23,2,4]]}    
    name = "RoboticBoltshooter"
    deck_name = "RoboticBoltshooter"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Multiple targets
        self.updateProperties(self.properties[level][elite], innate)     

class RuinedMachine(Monster):
    properties = {0:[[3,1,1],[5,1,2]], 1:[[5,1,1], [8,1,2]], 2:[[6,2,1],[9,2,2]], 3:[[6,2,2],[10,2,3]], \
        4:[[8,2,2],[13,2,3]], 5:[[10,2,2],[15,3,3]], 6:[[12,2,3],[18,3,4]], 7:[[15,3,3],[22,4,4]]}    
    name = "RuinedMachine"
    deck_name = "RuinedMachine"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #Immune to poison
        self.updateProperties(self.properties[level][elite], innate)

class SavvasIcestorm(Monster):
    properties = {0:[[7,2,2],[12,2,3]], 1:[[10,2,2], [12,2,3]], 2:[[12,3,2],[15,3,3]], 3:[[12,3,2],[17,3,4]], \
        4:[[13,3,3],[17,4,4]], 5:[[15,3,4],[20,4,5]], 6:[[16,4,4],[26,4,6]], 7:[[20,4,5],[33,4,7]]} 
    name = "SavvasIcestorm"
    deck_name = "SavvasIcestorm"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #Immune to poison
        self.updateProperties(self.properties[level][elite], innate)
    
class SavvasLavaflow(Monster):
    properties = {0:[[8,3,2],[13,3,3]], 1:[[9,3,2], [15,3,3]], 2:[[11,3,3],[18,3,3]], 3:[[14,3,3],[21,3,4]], \
        4:[[16,3,4],[25,4,4]], 5:[[20,3,4],[30,4,5]], 6:[[28,4,4],[40,4,6]], 7:[[35,4,5],[50,4,7]]} 
    name = "SavvasLavaflow"
    deck_name = "SavvasLavaflow"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" #Immune to poison
        self.updateProperties(self.properties[level][elite], innate)

class ShrikeFiend(Monster):
    properties = {0:[[6,1,2],[8,2,3]], 1:[[8,1,2],[10,2,3]], 2:[[9,1,3],[12,2,4]], 3:[[10,2,3],[16,2,4]], \
        4:[[13,2,3],[20,2,5]], 5:[[15,2,4],[25,3,5]], 6:[[21,3,4],[33,3,6]], 7:[[29,3,4],[45,3,6]]} 
    name = "ShrikeFiend"
    deck_name = "ShrikeFiend"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)

class SnowImp(Monster):
    properties = {0:[[2,2,1],[4,2,2]], 1:[[2,2,1],[4,2,2]], 2:[[3,2,1],[5,3,2]], 3:[[3,2,2],[7,3,2]], \
        4:[[4,2,2],[8,3,3]], 5:[[5,3,2],[10,4,3]], 6:[[7,3,3],[13,4,4]], 7:[[11,3,3],[18,4,4]]} 
    name = "SnowImp"
    deck_name = "Imp"
    num_standees = 10
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
    
class SpittingDrake(Monster):
    properties = {0:[[4,3,3],[7,3,4]], 1:[[5,3,3],[9,3,4]], 2:[[7,3,3],[10,3,5]], 3:[[8,3,4],[13,3,5]], \
        4:[[9,4,4],[16,4,5]], 5:[[12,4,4],[19,4,6]], 6:[[16,4,5],[27,4,6]], 7:[[22,4,5],[34,4,7]]} 
    name = "SpittingDrake"
    deck_name = "SpittingDrake"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Muddle 
        self.updateProperties(self.properties[level][elite], innate)

class SteelAutomaton(Monster):
    properties = {0:[[9,1,3],[10,2,4]], 1:[[9,2,3],[12,2,4]], 2:[[12,2,3],[14,2,5]], 3:[[14,2,4],[17,3,5]], \
        4:[[18,2,4],[22,3,5]], 5:[[21,3,4],[25,3,6]], 6:[[22,3,4],[26,3,7]], 7:[[27,4,5],[36,4,7]]} 
    name = "SteelAutomaton"
    deck_name = "SteelAutomaton"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Immune to poison and disarm. Shield varies
        self.updateProperties(self.properties[level][elite], innate)

class SunDemon(Monster):
    properties = {0:[[5,2,2],[9,2,3]], 1:[[8,2,2],[12,2,3]], 2:[[10,2,2],[13,2,4]], 3:[[11,2,3],[16,3,4]], \
        4:[[13,3,3],[18,3,5]], 5:[[13,3,3],[18,3,5]], 6:[[16,3,4],[25,4,5]], 7:[[19,3,5],[27,4,6]]} 
    name = "SunDemon"
    deck_name = "SunDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Attacks have disadvantage, shield
        self.updateProperties(self.properties[level][elite], innate)

class VermlingPriest(Monster):
    properties = {0:[[2,2,1],[3,3,2]], 1:[[2,2,1],[3,3,2]], 2:[[3,2,1],[4,3,2]], 3:[[3,2,2],[5,3,3]], \
        4:[[3,3,2],[5,3,3]], 5:[[4,3,3],[6,3,4]], 6:[[5,3,4],[8,3,5]], 7:[[8,3,4],[11,3,5]]} 
    name = "VermlingPriest"
    deck_name = "Priest"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Attacks have disadvantage, shield
        self.updateProperties(self.properties[level][elite], innate)

class VermlingScout(Monster):
    properties = {0:[[2,3,1],[4,3,2]], 1:[[3,3,1],[5,3,2]], 2:[[3,3,2],[5,4,3]], 3:[[4,3,2],[7,4,3]], \
        4:[[5,3,3],[8,4,4]], 5:[[7,3,3],[11,4,4]], 6:[[10,4,3],[16,5,4]], 7:[[15,4,3],[23,5,4]]} 
    name = "VermlingScout"
    deck_name = "Scout"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = "" # Attacks have disadvantage, shield
        self.updateProperties(self.properties[level][elite], innate)
        
class WindDemon(Monster):
    properties = {0:[[3,3,2],[5,4,3]], 1:[[3,3,2],[5,3,3]], 2:[[4,4,2],[7,4,3]], 3:[[5,4,3],[8,4,4]], \
        4:[[7,4,3],[10,4,5]], 5:[[10,4,3],[14,4,5]], 6:[[11,4,3],[16,4,5]], 7:[[14,4,4],[21,4,6]]} 
    name = "WindDemon"
    deck_name = "WindDemon"
    num_standees = 6
    def __init__(self, level, elite=0):
        super().__init__(level, self.name, elite, self.deck_name)
        innate = ""
        self.updateProperties(self.properties[level][elite], innate)
    
        
        
        
        
        
        
        