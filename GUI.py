# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:15:22 2023

@author: blake
"""


import PySimpleGUI as sg
import traceback
from Game import Game
import os
import io
from PIL import Image, ImageTk



n_rows, n_cols = 2, 4
sg.theme('Dark Blue 3')  # please make your windows colorful
monsters = ["AlgoxArcher", "AlgoxGuard", "AlgoxScout"]


def get_img_data(f, maxsize=(150, 150), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

class MonsterImage():
    def __init__(self, name='Default', monster=None, row=0, col=0):
        self.image_elem = sg.Image(data=get_img_data(os.path.join('MonsterImages',name+'.webp'),first=True),key='Image'+str(row)+str(col))
        health = 0
        if monster is not None:
            health = monster.health
        self.spin = sg.Spin([x for x in range(health+1)], health, key='Spin'+str(row)+str(col))
row0, row1 = [], []
for i in range(n_cols):
    im = MonsterImage(row=0,col=i)
    row0.append(im.image_elem)
    row0.append(im.spin)
    im = MonsterImage(row=1,col=i)
    row1.append(im.image_elem)
    row1.append(im.spin)
    
layout = [
    [row0],
    [row1],
    [sg.Text('Output: '), sg.Text(size=(30,1), key='-OUTPUT-')],
    [sg.Button('AddMonster'), sg.OptionMenu(monsters,key='MonsterToAdd'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteAdd')],
    [sg.Button('RemoveMonster'), sg.OptionMenu(monsters,key='MonsterToRemove'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteRemove')],
    [sg.Button("StartGame"), sg.Combo([x for x in range(9)],key='level'), sg.Button('Exit')]
    ]

window = sg.Window('Window Title', layout)
game = None
curr_row, curr_col = 0, 0
 
while True:  # Event Loop
    try:
        event, values = window.read()
        print(event, values)
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit'):# and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break
        if event == 'StartGame':
            print("Values level ", values['level'], type(values['level']))
            if values['level'] == "":
                window['-OUTPUT-'].update("level not set")
                continue
            game = Game(values['level'])
            window['-OUTPUT-'].update("Started game at level {}".format(values['level']))
        elif game is None:
            continue
        
        if event == 'AddMonster':
            if values['MonsterToAdd'] =="" or values['EliteAdd'] == "":
                window['-OUTPUT-'].update("Monster information not set")
                continue
            elite = 0
            if values['EliteAdd'] == 'Elite':
                elite = 1
            game.addMonster(values['MonsterToAdd'], elite)
            monster_image = MonsterImage(values['MonsterToAdd'], game.getMonsterInstance(values['MonsterToAdd']), curr_row, curr_col)
            print("type(window_image) ", type(window['Image'+str(curr_row)+str(curr_col)]))
            print("type monster_image.image_elem ", type(monster_image.image_elem))
            window['Image'+str(curr_row)+str(curr_col)].update(monster_image.image_elem.Data, size=(150,150))
            window['Spin'+str(curr_row)+str(curr_col)].update(monster_image.spin.DefaultValue, monster_image.spin.Values)
            curr_col += 1
            if curr_col >= n_cols:
                curr_col = 0
                curr_row += 1
            
        if event =='RemoveMonster':
            if values['MonsterToRemove'] =="" or values['EliteRemove'] == "":
                window['-OUTPUT-'].update("Monster information not set")
                continue
            elite = 0
            if values['EliteRemove'] == 'Elite':
                elite = 1
            game.removeMonster(values['MonsterToRemove'], elite)
    except:
        print('\n\n')
        traceback.print_exc()
        break
        
         
window.close()
