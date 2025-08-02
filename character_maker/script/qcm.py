# -*- coding: utf-8 -*-
from .class_character import *
from .class_arme import *
from .class_armure import *

"""
    Ce scripte à pour but de créer un personnage de Dungeons & Dragons
    en possant des questions à l'utilisateur.

    Ce système de création de personnage est inspiré du questionnaire de Daggerfall.
    Le joueur ne choisit pas la race, la classe, l'alignement, etc. de son personnage,
    ce sont ses réaction a des évenement qui les détermineront.

    Les questions met le jour dans la peau d'un personnage fictif, ces actions et ses choix
    détermineront la race, la classe, l'alignement, etc. de son personnage.

    Il utilise la classe Character pour stocker les données du personnage.
"""

def qcm():
    """Lance le questionnaire de création de personnage"""
    character = Character()
    classe = list()
    alignement = list()
    historique = list()
    
    print("Bienvenue dans le questionnaire de création de personnage Dungeons & Dragons.")
    
    character.data["name"] = input("Quel est le nom de votre personnage ? ")
    character.data["level"] = int(input("Quel est le niveau de votre personnage ? "))

    print(
        "Question 1 : L’Enfance\n",
        "Tu es un enfant dans un village isolé. Un étranger blessé arrive en titubant à la tombée de la nuit. Il demande de l'aide. Que fais-tu ?\n",
        "\n",
        "1. Je cours chercher un adulte.\n",
        "2. Je le soigne moi-même avec ce que je trouve.\n",
        "3. Je le fouille discrètement pour voir s’il a quelque chose d'intéressant.\n",
        "4. Je le menace de s'éloigner : il pourrait être dangereux."
    )
    choi_1 = int(input("Choix (1-4) :\n>>> "))
    # 1. +1 Sagesse, Historique : Villageois ou Acolyte
    if choi_1 == 1:
        character.data["stat_sagesse"] += 1
        historique.append("Villageois")
        historique.append("Acolyte")
    # 2. +1 Intelligence, Médecine
    elif choi_1 == 2:
        character.data["stat_intelligence"] += 1
        character.data["competence_medic"] = True
    # 3. +1 Dextérité, Alignement : Chaotique Neutre
    elif choi_1 == 3:
        character.data["stat_dexterity"] += 1
        character.data["alignment"] = "Chaotique Neutre"
        historique.append("Voleur")
    # 4. +1 Force, Alignement : Loyal Neutre ou Loyal Mauvais
    elif choi_1 == 4:
        character.data["stat_force"] += 1
        alignement.append("Loyal Neutre")
        alignement.append("Loyal Mauvais")    
    #   Question 2
    print(
        "Question 2 : Le Conflit\n",
        "Une bande de brigands menace ton village. Tu es assez jeune mais motivé à agir. Quelle est ta réponse ?\n",
        "\n",
        "1. J'organise la défense avec les anciens et les chasseurs.\n",
        "2. Je prépare un piège dans les bois, sans en parler à personne.\n",
        "3. Je propose de négocier avec les brigands."
        "4. Je m’enfuis discrètement la nuit avec mes proches."
    )
    choi_2 = int(input("Choix (1-4) :\n>>> "))
    # 1. Classe probable : Paladin ou Guerrier, Alignement : Loyal Bon
    if choi_2 == 1:
        classe.append("Paladin")
        classe.append("Guerrier")
        alignement.append("Loyal Bon")
    # 2. Classe probable : Rôdeur ou Voleur, Alignement : Neutre
    elif choi_2 == 2:
        classe.append("Rôdeur")
        classe.append("Voleur")
        alignement.append("Neutre")
    # 3. +1 Charisme, Classe possible : Barde ou Ensorceleur
    elif choi_2 == 3:
        character.data["stat_charisme"] += 1
        classe.append("Barde")
        classe.append("Ensorceleur")
    # 4. Historique : Réfugié, Alignement : Neutre Bon
    elif choi_2 == 4:
        historique.append("Réfugié")
        alignement.append("Neutre Bon")