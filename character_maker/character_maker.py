# jdr tools\character_maker\character_maker.py
# -*- coding: utf-8 -*-
from random import randint
from .script import etape_par_etape 

print(
    "Bienvenu dans le 'Character_Maker' un outil de création de personnage DnD.\n",
    "Pour commencer comment voulez-vous créer votre personnage ?"
)
start = input(
    "1 : étape par étape\n2 : par un questionnaire\n3 : manuellement\n>>> "
)
if start == "1":
    print("Vous avez choisi de créer votre personnage étape par étape.")
    etape_par_etape.etape_par_etape_RUN()
elif start == "2":
    print("Vous avez choisi de créer votre personnage par un questionnaire.")
    from .script import qcm
    qcm.qcm()