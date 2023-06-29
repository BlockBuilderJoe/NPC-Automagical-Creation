# NPC Automagical Creation
Automates the creation of NPC's in Minecraft Bedrock and Education by doing the following: 

 1. Writes the scene.json file.
 2. Writes a text file called README.txt that contains the commands to make the npc's appear in game.
 3. Writes a reloadnpc.mcfunction to automate the reloading of NPC's.
l

# Requirements

```
pip install pandas openpyxl
```

# How to use

1. Fill out the excel template in templates and then put it in the root of the folder.
2. Run the ClickMe.py.
3. Copy the scene.json to the dialogue folder in your behaviour packs.
4. Copy the reloadnpc.mcfunction to the function folder into your behaviour packs.
5. Open Minecraft up.
6. Follow the instructions in README.txt to create your npc's.
7. If you make any changes to the npc.xlsx run through step 1 - 6 again and then type function reloadnpc in game to update your changes. 
