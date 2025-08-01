# jdr tools\character_maker\character_maker.py
# -*- coding: utf-8 -*-
from random import randint
# importe la classe Character
from script.class_character import *

import script.etape_par_etape


print(
    "Bienvenu dans le 'Character_Maker' un outil de création de personnage DnD.\n",
    "Pour commencer comment voulez-vous créer votre personnage ?"
)
start = input(
    "1 : étape par étape\n2 : par un questionnaire\n3 : manuellement\n>>> "
)
if start == "1":
    print("Vous avez choisi de créer votre personnage étape par étape.")
    script.etape_par_etape.main()
