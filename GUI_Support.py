# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:55:20 2023

@author: blake
"""

import PySimpleGUI as sg
from PIL import Image, ImageEnhance, ImageOps
import os
import io
import numpy as np

from Monsters import Monster
from GUI_config import n_rows, n_cols

Strengthen_f0 = './ConditionImages/Strengthen0.png'
Strengthen_f1 = './ConditionImages/Strengthen1.png'
Stun_f0 = './ConditionImages/Stun0.png'
Stun_f1 = './ConditionImages/Stun1.png'
Poison_f0 = './ConditionImages/Poison0.png'
Poison_f1 = './ConditionImages/Poison1.png'
Muddle_f0 = './ConditionImages/Muddle0.png'
Muddle_f1 = './ConditionImages/Muddle1.png'
Invisible_f0 = './ConditionImages/Invisible0.png'
Invisible_f1 = './ConditionImages/Invisible1.png'
Disarm_f0 = './ConditionImages/Disarm0.png'
Disarm_f1 = './ConditionImages/Disarm1.png'
Brittle_f0 = './ConditionImages/Brittle0.png'
Brittle_f1 = './ConditionImages/Brittle1.png'
Wound_f0 = './ConditionImages/Wound0.png'
Wound_f1 = './ConditionImages/Wound1.png'
CONDITION_NAMES = ['Strengthen', 'Stun', 'Poison', 'Muddle', 'Invisible', 'Disarm', 'Brittle', 'Wound']
CONDITION_IMG_SIZE = (24,24)

def loadImage(monster, maxsize=(150, 150)):
    """Generate image data using PIL
    """
    img = Image.open(os.path.join('MonsterImages',monster.name+'.webp'))
    if 'Default' in monster.name:
        img = ImageEnhance.Color(img).enhance(1.5)
        img.thumbnail(maxsize)
    else:
        img.thumbnail(maxsize)
        if monster.elite:
            img = ImageOps.expand(img, border=5,fill=('yellow'))
        num = Image.open(os.path.join('MonsterImages',str(monster.standee)+'.jpg'))
        num.thumbnail((25,25))
        num = num.convert('RGBA')
        # img = img.convert('RGBA')
        s = img.size
        img.paste(num, (s[0]-25, 0), num)
    
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
    # return ImageTk.PhotoImage(img)

def calc_row_col(i):
    return i // n_cols, i % n_cols

def monsterUI(frame):
    cond_buttons = np.array([x.button for x in frame.conditions.values()])
    cond_buttons = np.reshape(cond_buttons, (2, len(cond_buttons)//2))
    return frame.image_elem, sg.Col([[frame.spin], [frame.remove], [sg.Col(cond_buttons)]])

class condition():
    def __init__(self, name, button, active):
        self.name = name
        self.button = button
        self.active = active
        self.fname = globals()[self.name+'_f0']
        
    def flip(self):
        if self.active:
            self.active = False
            self.fname = globals()[self.name+'_f0']
        else:
            self.active = True
            self.fname = globals()[self.name+'_f1']
        return self.fname
    
    def copy_from(self, other):
        self.fname = other.fname
        self.button.ImageData = other.button.ImageData
        self.button.image_size = CONDITION_IMG_SIZE
        self.active = other.active

class MonsterFrame():
    def __init__(self, name='Default', standee=None, monster=Monster(), i=0):
        self.name = name
        self.monster = monster
        self.image_elem = sg.Image(data=loadImage(monster),key='Image'+str(i))
        health = 0
        if monster is not None:
            health = monster.health
        self.spin = sg.OptionMenu([x for x in range(health+1)], health, key='Spin'+str(i), size=(8,8))
        self.remove = sg.Button('Remove',key='Remove'+str(i))
        self.conditions = {name : condition(name, 
                                            sg.Button(image_filename=globals()[name+'_f0'],
                                                      key=f'Condition_{name}_{str(i)}',
                                                      image_size=CONDITION_IMG_SIZE), False) for name in CONDITION_NAMES}
    
    def copy_from(self, other, val, i):
        self.name = other.name
        self.monster = other.monster
        self.image_elem = other.image_elem
        self.spin = sg.OptionMenu(other.spin.Values, val, key='Spin'+str(i),size=(8,8),auto_size_text=True)
        for name, cond in other.conditions.items():
            self.conditions[name].button.image_file_name=cond.fname
            self.conditions[name].copy_from(cond)
        
def monsterMoveImages(window, values, frames, delete_i):
    print("Deleting ", delete_i, " \n", [x.monster.standee for x in frames])
    for i in range(delete_i, n_rows*n_cols):
        if i == n_rows*n_cols - 1:
            val = None
            frame = MonsterFrame(i=i)
        else:
            val = values['Spin'+str(i+1)]
            frame = frames[i+1]
            
        frames[i].copy_from(frame, val, i)
        
        # frames[i].name = frame.name
        # frames[i].standee = frame.standee
        # frames[i].image_elem.Data = frame.image_elem.Data
        window['Image'+str(i)].update(frame.image_elem.Data, size=(150,150))
    
        # frames[i].spin = sg.OptionMenu(frame.spin.Values, val, key='Spin'+str(i),size=(8,8),auto_size_text=True)
        for name, cond in frame.conditions.items():
            window[f'Condition_{name}_{i}'].update(image_filename=cond.fname, image_size=CONDITION_IMG_SIZE)
        #     frames[i].conditions[name].button.image_filename=cond.fname
        #     frames[i].conditions[name].copy_from(cond)
        window['Spin'+str(i)].update(val, frame.spin.Values)
    print([x.monster.standee for x in frames])
    window.refresh()
        
def checkRemove(frames, monster):
    names = [x.name for x in frames]
    if len(np.where(names)[0]) == 1:
        return True
    return False
        
