import yaml
import os

def load_yaml(filename):
    return yaml.safe_load(open(filename))

def dump_yaml(yml, fname):
    yaml.dump(yml, open(fname, 'w'), sort_keys=False)
    

def change_Name_number(name, number):
    return name[name.rfind('_'):] + str(number) + '$'

def change_attr(attr_name, change_func):
    os.chdir('C:\Program Files (x86)\Steam\steamapps\common\Gloomhaven\SteamMods\TimeSeerGlobal\ModdedYML\AbilityCard')
    for i, file in enumerate(os.listdir()):
        print(file)
        yml = load_yaml(file)
        name = '$ABILITY_CARD_timeseer'+str(i+1)+'$'
        yml['Name'] = name
        dump_yaml(yml, file)
        
        