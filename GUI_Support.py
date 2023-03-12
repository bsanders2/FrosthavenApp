# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:55:20 2023

@author: blake
"""

import PySimpleGUI as sg
from PIL import Image, ImageEnhance
import os
import io
import numpy as np

from GUI_config import n_rows, n_cols

def loadImage(name, standee_num, maxsize=(150, 150)):
    """Generate image data using PIL
    """
    img = Image.open(os.path.join('MonsterImages',name+'.webp'))
    if 'Default' in name:
        img = ImageEnhance.Color(img).enhance(1.5)
    else:
        num = Image.open(os.path.join('MonsterImages',str(standee_num)+'.jpg'))
        num.thumbnail((25,25))
        num = num.convert('RGBA')
        # img = img.convert('RGBA')
        s = img.size
        img.paste(num, (s[0]-25, 0), num)
    img.thumbnail(maxsize)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
    # return ImageTk.PhotoImage(img)

def calc_row_col(i):
    return i // n_cols, i % n_cols

def monsterUI(frame):
    return frame.image_elem, sg.Col([[frame.spin], [frame.remove]])

class MonsterFrame():
    def __init__(self, name='Default', standee=None, monster=None, i=0):
        self.name = name
        self.monster = monster
        self.standee = standee
        self.image_elem = sg.Image(data=loadImage(name,standee),key='Image'+str(i))
        health = 0
        if monster is not None:
            health = monster.health
        self.spin = sg.OptionMenu([x for x in range(health+1)], health, key='Spin'+str(i), size=(8,8),auto_size_text=True)
        self.remove = sg.Button('Remove',key='Remove'+str(i))
        
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
        
