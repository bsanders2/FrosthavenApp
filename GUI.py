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
from copy import copy
from PIL import Image, ImageTk
import numpy as np



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

def calc_row_col(i):
    return i // n_cols, i % n_cols

class MonsterFrame():
    def __init__(self, name='Default', monster=None, i=0):
        self.name = name
        self.image_elem = sg.Image(data=get_img_data(os.path.join('MonsterImages',name+'.webp'),first=True),key='Image'+str(i))
        health = 0
        if monster is not None:
            health = monster.health
            print("monster health: ", health)
        self.spin = sg.Spin([x for x in range(health+1)], health, key='Spin'+str(i),expand_x=True, expand_y=True)
        self.remove = sg.Button('Remove',key='Remove'+str(i))

def monsterMoveImages(window, delete_i):
    default = MonsterFrame()

    print("==default before remove\n",[frames[i].image_elem.Data == default.image_elem.Data for i in range(8)])
    for i in range(delete_i, n_rows*n_cols):
        print("i ", i, "  ", frames[i].name)
        if i == n_rows*n_cols - 1:
            frame = MonsterFrame(i=i)
        else:
            frame = frames[i+1]
        frames[i].name = frame.name
        frames[i].image_elem.Data = frame.image_elem.Data
        window['Image'+str(i)].update(frame.image_elem.Data, size=(150,150))
        if frame.spin.TKStringVar is not None:
            val = frame.spin.get()
            print("entered get")
        else:
            val = frame.spin.DefaultValue
            print("entered default")
        frames[i].spin.value = val
        frames[i].spin.values = frame.spin.Values
        window['Spin'+str(i)].update(val, frame.spin.Values)
            
    
frames = [MonsterFrame(i=i) for i in range(n_cols*n_rows)]
def monsterUI(frame):
    return frame.image_elem, sg.Pane([sg.Col([[frame.spin]]), sg.Col([[frame.remove]])])
    
layout = [
    np.concatenate([monsterUI(x) for x in frames[:n_cols]]),
    np.concatenate([monsterUI(x) for x in frames[n_cols:]]),
    [sg.Text('Output: '), sg.Text(size=(30,1), key='-OUTPUT-')],
    [sg.Button('AddMonster'), sg.OptionMenu(monsters,key='MonsterToAdd'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteAdd')],
    [sg.Button('RemoveMonster'), sg.OptionMenu(monsters,key='MonsterToRemove'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteRemove')],
    [sg.Button("StartGame"), sg.Combo([x for x in range(9)],key='level'), sg.Button('Exit')]
    ]

window = sg.Window('Window Title', layout,)
window.finalize()
game = None
curr_i = 0
 
while True:  # Event Loop
    try:
        event, values = window.read()
        curr_row, curr_col = calc_row_col(curr_i)
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
            frame = MonsterFrame(values['MonsterToAdd'], game.getMonsterInstance(values['MonsterToAdd']), curr_i)
            frames[curr_i] = frame
            window['Image'+str(curr_i)].update(frame.image_elem.Data, size=(150,150))
            
            default = MonsterFrame()
            print("==default after add\n",[window['Image'+str(i)].Data == default.image_elem.Data for i in range(8)])
            
            window['Spin'+str(curr_i)].update(frame.spin.DefaultValue, frame.spin.Values)
            curr_i += 1
            
        # if event =='RemoveMonster':
        #     if values['MonsterToRemove'] =="" or values['EliteRemove'] == "":
        #         window['-OUTPUT-'].update("Monster information not set")
        #         continue
        #     elite = 0
        #     if values['EliteRemove'] == 'Elite':
        #         elite = 1

        if 'Remove' in event:
            # need a list of the current monsters in each slot so we know if
            # we need to call game.removeMonster
            delete_i = int(event[-1])
            default = MonsterFrame()
            if delete_i > curr_i or curr_i == 0:
                window['-OUTPUT-'].update("Cannot remove monster that's not there")
                continue
            monsterMoveImages(window, delete_i)
            game.removeMonster(values['MonsterToRemove'], elite)
            curr_i -= 1
            window['-OUTPUT-'].update("Removed monster {}".format(delete_i))
            window.refresh()
            
            
    except:
        print('\n\n')
        traceback.print_exc()
        break
        
         
window.close()
