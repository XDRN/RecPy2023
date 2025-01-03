import os
import data

from RecNet import AvatarItemGen, Skins

def setUp():
    print("Setting up... (May take a minute to download everything.)")
    os.mkdir(f"{data.saveDataPath}")
    os.mkdir(f"{data.saveDataPath}Profile")
    AvatarItemGen.gen("AvatarItemWardrobeRuntimeConfig.json", f"{data.saveDataPath}AvatarItems.json")
    Skins.gen(f"{data.saveDataPath}Equipments.json")

setUp()