# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:15:22 2023

@author: blake
"""


import PySimpleGUI as sg
import traceback


# other packages
import numpy as np

# repo packages
from Game import Game
from GUI_Support import MonsterFrame, checkRemove, monsterMoveImages, monsterUI
from GUI_config import n_rows, n_cols

monsters = ["AlgoxArcher", "AlgoxGuard", "AlgoxScout"]

frames = [MonsterFrame(i=i) for i in range(n_cols*n_rows)]

layout = [
    np.concatenate([monsterUI(x) for x in frames[:n_cols]]),
    np.concatenate([monsterUI(x) for x in frames[n_cols:]]),
    [sg.Text('Output: '), sg.Text(size=(30,1), key='-OUTPUT-')],
    [sg.Button('AddMonster'), sg.OptionMenu(monsters,key='MonsterToAdd'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteAdd')],
    [sg.Button('RemoveMonster'), sg.OptionMenu(monsters,key='MonsterToRemove'), sg.OptionMenu(['Normal', 'Elite'],'Normal',key='EliteRemove')],
    [sg.Button("StartGame"), sg.Combo([x for x in range(9)],key='level'), sg.Button('Exit')]
    ]

window = sg.Window('Window Title', layout, finalize=True)
# window.finalize()
game = None
curr_i = 0
 
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
            monster = game.addMonster(values['MonsterToAdd'], elite)
            if monster is None: # out of standees for this monster
                window['-OUTPUT-'].update("Out of standees for {}".format(values['MonsterToAdd']))
                continue
            frame = MonsterFrame(values['MonsterToAdd'], monster.standee, monster, curr_i)
            window['-OUTPUT-'].update("Added {} : {} at frame {}".format(values['MonsterToAdd']+' '+['Normal','Elite'][elite], frame.monster.standee, curr_i))
            frames[curr_i] = frame
            window['Image'+str(curr_i)].update(frame.image_elem.Data, size=(150,150))
            window['Spin'+str(curr_i)].update(frame.spin.DefaultValue, frame.spin.Values, size=(8,8))
            curr_i += 1

        if 'Remove' in event:
            delete_i = int(event[-1])
            default = MonsterFrame()
            if delete_i > curr_i or delete_i == curr_i == 0:
                window['-OUTPUT-'].update("Cannot remove monster that's not there")
                continue
            game.removeMonster(frames[delete_i].monster)    
            monsterMoveImages(window, values, frames, delete_i)
            curr_i -= 1
            window['-OUTPUT-'].update("Removed monster {}".format(delete_i))
            
            
    except:
        print('\n\n')
        traceback.print_exc()
        break
        
         
window.close()
