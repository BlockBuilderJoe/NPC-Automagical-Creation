############################################### Imports dependencies ##########################################################################################################################################
import pandas as pd
import json

#import openpyxl

#get the location of the scriptss
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rel_path = "npc.xlsx"
abs_file_path = os.path.join(script_dir, rel_path)

##############################################  Inputs ###################################################################################################Minecraft_version = 1.17
Minecraft_version = str(1.17)
############################################## Prepares CSV File for future processing ##################################################################################################

npc_template = pd.read_excel(abs_file_path)  # Reads the Excel chart 
npc_template = pd.DataFrame(npc_template)  #Make a dataframe
#npc_template = npc_template.apply(lambda x: pd.Series(x.dropna().values)) # Drops NA
npc_template = npc_template.fillna('') # Fills NaN with empty strings 


################ Splits the commands columns by ", " and makes them into a python list  #########################################################

on_open_commands = npc_template.iloc[:,4].str.split(', ')
on_close_commands = npc_template.iloc[:,5].str.split(', ')
commands_1 = npc_template.iloc[:,7].str.split(', ')
commands_2 = npc_template.iloc[:,9].str.split(', ')
commands_3 = npc_template.iloc[:,11].str.split(', ')
commands_4 = npc_template.iloc[:,13].str.split(', ')
commands_5 = npc_template.iloc[:,15].str.split(', ')
commands_6 = npc_template.iloc[:,17].str.split(', ')

############################################## Count and for loop prep ##########################################################################################################################################


row_count = 0  # Creates the row count for reference

scene_amount = len(npc_template)

scene = [] #Prepares a list for appending later on  

text = [] #Prepares a list for the text to be added later on. 

npcreload = [] #Prepares a list for the text to be added later on.
############################################## Runs through the rows formatting a json file ##########################################################################################################################################

for index, row in npc_template.iterrows(): # Runs through the rows and creates a new list
    print(row_count)
    buttons1 = {
        "name": npc_template.iloc[:,6][row_count], 
        "commands": commands_1[row_count]
    }
    buttons2 = {
        "name": npc_template.iloc[:,8][row_count], 
        "commands": commands_2[row_count]
    }
    buttons3 = {
        "name": npc_template.iloc[:,10][row_count], 
        "commands": commands_3[row_count]
    }
    buttons4 = {
        "name": npc_template.iloc[:,12][row_count], 
        "commands": commands_4[row_count]
    }
    buttons5 = {
        "name": npc_template.iloc[:,14][row_count], 
        "commands": commands_5[row_count]
    }
    buttons6 = {
        "name": npc_template.iloc[:,16][row_count], 
        "commands": commands_6[row_count]
    }
    #replace apostrophes with apostrophes
    npc_template.iloc[:,3][row_count] = npc_template.iloc[:,3][row_count].replace("’", "'")
    npc_template.iloc[:,3][row_count] = npc_template.iloc[:,3][row_count].replace("‘", "'")
    npc_template.iloc[:,3][row_count] = npc_template.iloc[:,3][row_count].replace(" ", "")
    npc_template.iloc[:,3][row_count] = npc_template.iloc[:,3][row_count].replace("...", f"...")

    
    #writes the json file
    scene.append({'scene_tag':npc_template.iloc[:,0][row_count], 'npc_name': npc_template.iloc[:,2][row_count], 'text':npc_template.iloc[:,3][row_count], 'on_open_commands': on_open_commands[row_count], 'on_close_commands': on_close_commands[row_count], "buttons": [buttons1, buttons2, buttons3, buttons4, buttons5, buttons6]})
    #writes the text file lines for each row in the excel.
    
    string = f"######################################################## \n INSTRUCTIONS FOR: \n NAME = {npc_template.iloc[:,2][row_count]} \n TAG = {npc_template.iloc[:,1][row_count]} \n \n 1. Stand in front of the NPC and copy this command: \n \n /tag @e[type=npc, r=2] add {npc_template.iloc[:,1][row_count]} \n \n 2. Then paste this command: \n \n /dialogue change @e[tag={npc_template.iloc[:,1][row_count]}] {npc_template.iloc[:,0][row_count]} \n \n ######################################################## \n "    
    text.append(string)

    NPC_reload = f"dialogue change @e[tag={npc_template.iloc[:,1][row_count]}] {npc_template.iloc[:,0][row_count]}"
    npcreload.append(NPC_reload)

    row_count = row_count + 1 # Increases the row count by 1
    
    if row_count == scene_amount: # Tests to see if its the final row
        break
######################################### Final formatting #############################################################################################################################################

scene = {"format_version": Minecraft_version, "minecraft:npc_dialogue":{"scenes": scene}}

with open(f'{os.path.dirname(__file__)}/scene.json', 'w', encoding='utf-8') as f:
    json.dump(scene, f, ensure_ascii=False, indent=4)

with open(f"{os.path.dirname(__file__)}/README.txt", "w") as f:
    f.write("\n".join(text))

with open(f"{os.path.dirname(__file__)}/reloadNPC.mcfunction", "w") as f:
    f.write("\n".join(npcreload))
    


    




