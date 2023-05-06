_MONSTER_NAMES_ = ["AbaelHerder","AlgoxArcher","AlgoxGuard", "AlgoxIcespeaker","AlgoxSnowspeaker","AncientArtillery",
                   "BurrowingBlade","ChaosDemon","CityGuard","DeepTerror","EarthDemon","FlameDemon","FlamingBladespinner",
                   "ForestImp","FrostDemon","FrozenCorpse","HarrowerInfester","Hound","IceWraith","LightningEel",
                   "LivingBones","LivingDoom","LivingSpirit","LurkerClawcrusher","LurkerMindsnipper","LurkerSoldier",
                   "LurkerWavethrower","NightDemon","Ooze","PiranhaPig","PolarBear","RendingDrake","RoboticBoltshooter",
                   "RuinedMachine","SavvasIcestorm","SavvasLavaflow","ShrikeFiend", "SnowImp", "SpittingDrake", "SteelAutomaton",
                   "SunDemon","VermlingPriest","VermlingScout","WindDemon"]
def importClasses():
    from importlib import import_module
    names_classes = {name : getattr(import_module('Monsters'), name) for name in _MONSTER_NAMES_}
    return names_classes