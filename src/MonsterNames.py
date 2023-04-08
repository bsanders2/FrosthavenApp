# _MONSTER_NAMES_ = ["AlgoxArcher", "AlgoxGuard", "AlgoxPriest", "AlgoxScout", "DeepTerror", "ForestImp", "FrozenCorpse", 
#                 "HarrowerInfester", "Hound", "IceWraith", "LurkerClawcrusher", "LurkerMindsnipper", "LurkerSoldier", 
#                 "NightDemon", "PolarBear", "ShrikeFiend", "SnowImp", "WindDemon"]
_MONSTER_NAMES_ = ["BurrowingBlade", "FlamingBladespinner", "ForestImp", 
                "HarrowerInfester", "Hound", "IceWraith", "LurkerClawcrusher", "LurkerSoldier",
                "NightDemon", "PiranhaPig", "PolarBear", "RuinedMachine", "ShrikeFiend", "SnowImp", "SpittingDrake", "SteelAutomaton", "WindDemon"]
def importClasses():
    from importlib import import_module
    classes = {name : getattr(import_module('Monsters'), name) for name in _MONSTER_NAMES_}
    return classes