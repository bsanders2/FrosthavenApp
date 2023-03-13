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

Wound_f0 = './ConditionImages/Wound0.png'
Wound_f1 = './ConditionImages/Wound1.png'

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
    return frame.image_elem, sg.Col([[frame.spin], [frame.remove], [x.button for x in frame.buttons.values()]])

class condition():
    def __init__(self, name, button, active):
        self.name = name
        self.button = button
        self.active = active
    def flip(self):
        if self.active:
            self.active = False
            return globals()[self.name+'_f0']
        else:
            self.active = True
            return globals()[self.name+'_f1']

class MonsterFrame():
    def __init__(self, name='Default', standee=None, monster=Monster(), i=0):
        self.name = name
        self.monster = monster
        self.standee = standee
        self.image_elem = sg.Image(data=loadImage(monster),key='Image'+str(i))
        health = 0
        if monster is not None:
            health = monster.health
        self.spin = sg.OptionMenu([x for x in range(health+1)], health, key='Spin'+str(i), size=(8,8))
        self.remove = sg.Button('Remove',key='Remove'+str(i))
        self.buttons = {'Wound':condition('Wound', sg.Button(image_filename=Wound_f0, key='Condition_Wound_'+str(i)), False)}
        
def monsterMoveImages(window, values, frames, delete_i):
    for i in range(delete_i, n_rows*n_cols):
        if i == n_rows*n_cols - 1:
            val = None
            frame = MonsterFrame(i=i)
        else:
            val = values['Spin'+str(i+1)]
            frame = frames[i+1]
        frames[i].name = frame.name
        frames[i].standee = frame.standee
        frames[i].image_elem.Data = frame.image_elem.Data
        window['Image'+str(i)].update(frame.image_elem.Data, size=(150,150))
    
        frames[i].spin = sg.OptionMenu(frame.spin.Values, val, key='Spin'+str(i),size=(8,8),auto_size_text=True)
        window['Spin'+str(i)].update(val, frame.spin.Values)
    window.refresh()
        
def checkRemove(frames, monster):
    names = [x.name for x in frames]
    if len(np.where(names)[0]) == 1:
        return True
    return False
        
