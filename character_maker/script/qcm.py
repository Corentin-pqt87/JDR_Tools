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
    race = list()
    
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
        character.data['competence_escamotage'] = True
        classe.append('Roublard')
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
        character.data["stat_constitution"] += 1
    # 2. Classe probable : Rôdeur ou Voleur, Alignement : Neutre
    elif choi_2 == 2:
        classe.append("Rôdeur")
        classe.append("Voleur")
        alignement.append("Neutre")
        character.data["stat_dexterity"] += 1
        character.data["competence_survie"] = True
    # 3. +1 Charisme, Classe possible : Barde ou Ensorceleur
    elif choi_2 == 3:
        character.data["stat_charisme"] += 1
        classe.append("Barde")
        classe.append("Ensorceleur")
        character.data["competence_tromperie"] = True
    # 4. Historique : Réfugié, Alignement : Neutre Bon
    elif choi_2 == 4:
        historique.append("Réfugié")
        alignement.append("Neutre Bon")
        character.data["competence_survie"] = True
        character.data["stat_sagesse"] += 1
    
    #   Question 3 : La Découverte
    print(
        "Question 3 : La Découverte\n",
        "Tu tombes par hasard sur un ancien livre couvert de symboles étranges. Que fais-tu ?\n\n",
        "1. Je l'étudie, fasciné\n",
        "2. Je le cache pour le vendre plus tard\n",
        "3. Je le brûle, par peur de la magie.\n",
        "4. Je le remets à une autorité religieuse."
    )
    choi_3 = int(input("Choix (1-4) :\n>>> "))
    #  1.  +2 Intelligence, Classe probable : Magicien
    if choi_3 == 1:
        character.data["stat_intelligence"] += 1
        classe.append("Magicien")
        character.data['competence_arcanes'] = True
    #  2.  +1 Intelligence, +1 Dextérité, Alignement : Chaotique Neutre
    elif choi_3 == 2:
        character.data["stat_intelligence"] += 1
        character.data["stat_dexterity"] += 1
        alignement.append('Chaotique Neutre')
    # 3. Alignement : Loyal Neutre ou Loyal Bon, Race : Naine possible
    elif choi_3 == 3:
        alignement.append("Loyal Neutre")
        alignement.append("Loyal Bon")
        race.append("Naine")
        race.append('Demi-orque')
        classe.append('Barbare')
        character.data["stat_force"] += 1
    # 4. Historique : Acolyte, Classe possible : Clerc, Alignement : Loyal Bon
    elif choi_3 == 4:
        historique.append("Acolyte")
        classe.append("Clerc")
        alignement.append("Loyal Bon")
        character.data["competence_religion"] = True
        character.data['stat_sagesse'] += 1
    
    #   Question 4 : La Trahison
    print(
        "Un ami d’enfance trahit ton groupe et rejoint un seigneur ennemi. Quelle est ta réaction ?\n\n",
        "1. Je pars à sa recherche pour comprendre son choix.\n",
        "2. Je jure de le tuer pour sa trahison.\n",
        "3. Je laisse faire, cela ne me concerne pas.\n",
        "4. Je tente de le convaincre de revenir."
    )
    choi_4 = int(input("Choix (1-4) :\n>>> "))
    #  1. +1 Charisme, Historique : Noble ou Héros du peuple
    if choi_4 == 1:
        character.data["stat_charisme"] += 1
        historique.append("Noble")
        historique.append("Héros du peuple")
        classe.append("Paladin")
        character.data["stat_charisme"] += 1
        character.data['competence_investigation'] = True
    # 2. Alignement : Neutre ou Mauvais, Classe : Guerrier ou Barbare
    elif choi_4 == 2:
        alignement.append("Neutre")
        alignement.append("Mauvais")
        classe.append("Guerrier")
        classe.append("Barbare")
        character.data["sauvegarde_force"] += 1
        race.append("Demi-orque")
    #  3.  Alignement : Neutre
    elif choi_4 == 3:
        alignement.append('Neutre')
        race.append('Humain')
        character.data['stat_constitution'] += 1
    #  4.  +1 Charisme, Classe : Barde ou Clerc
    elif choi_4 == 4:
        character.data["stat_charisme"] += 1
        classe.append('Classe')
        classe.append('Clerc')
        character.data['competence_persuasion'] = True
    
    #   Question 5 : Le Sang
    print(
        "On t’annonce que tu es issu d’un peuple ancien, aux pouvoirs étranges. Quelle est ta réaction ?\n\n",
        "1. J’embrasse cet héritage\n",
        "2. Je nie cette vérité, préférant mon identité actuelle.\n",
        "3. Je l’utilise à mon avantage.\n",
        "4. Je pars à la recherche d’autres comme moi."
    )
    choi_5 = int(input("Choix (1-4) :\n>>> "))
    #  1   Race : Demi-elfe, Tieffelin ou Drakéide selon autres réponses
    if choi_5 == 1:
        if 'Humain' in race:
            race.append('Demi-elfe')
        elif character.data['sauvegarde_constitution'] >= 3:
            race.append('Drakéide')
        else:
            race.append('Tieffelin')
        character.data["stat_sagesse"] += 1
    # 2  Alignement : Loyal, Race : Humaine ou Demi-orque
    elif choi_5 == 2:
        alignement.append('Loyal')
        race.append('Humain')
        race.append('Demi-orque') 
        race.append('Nain')    
    #  3  Alignement : Chaotique, Classe : Sorcier
    elif choi_5 == 3:
        alignement.append('Chaotique')
        classe.append('occultiste')
    #  4  Historique : Sage ou Ermite, Race : dépendante
    elif choi_5 == 4:
        historique.append('Sage')
        historique.append('Ermite')
    
    # Question 6 : Le Savoir
    print(
        "Un vieux professeur te propose de t’enseigner tout ce qu’il sait, mais il ne reste qu’un mois à vivre. Que fais-tu ?\n\n",
        "1. J’étudie sans relâche, quitte à m’épuiser.\n",
        "2. Je choisis un sujet qui me passionne et me concentre dessus.\n",
        "3. Je passe du temps avec lui à échanger sur la vie.\n",
        "4. Je vole ses notes et pars. Je n’ai pas le temps d’attendre."
    )
    choi_6 = int(input("Choix (1-4) :\n>>> "))
    #  1  +1 Intelligence, compétence : Arcanes, outils : calligraphie
    if choi_6 == 1:
        character.data['stat_intelligence'] += 1
        if character.data['competence_arcanes'] == True:
            character.data['stat_intelligence'] += 1
        else:
            character.data['competence_arcanes'] = True
        classe.append('Magicien')
    #  2  +1 Intelligence, compétence au choix : Nature, Histoire, Religion ou Investigation
    elif choi_6 == 2:
        character.data['stat_intelligence'] += 1
        print(
            "Vous avez le choix entre :\n",
            "1. Les savoirs et arts de la nature\n",
            "2. Les histoire du passé\n",
            "3. Les forces qui érige ce monde\n",
            "4. Les savoires interdit de sciences social"
        )
        choi_6_ = int(input("Choix (1-4) :\n>>> "))
        if choi_6_ == 1:
            classe.append('Druide')
            if character.data['competence_nature'] == True:
                character.data['stat_sagesse'] += 1
            else:
                character.data['competence_nature'] = True
        elif choi_6_ == 2:
            character.data['stat_sagesse'] += 1
            if character.data['competence_histoire'] == True:
                character.data['stat_sagesse'] += 1
            else:
                character.data['competence_histoire'] = True
        elif choi_6_ == 3:
            classe.append('Clerc')
            classe.append('Paladin')
            if character.data['competence_religion'] == True:
                character.data['stat_charisme'] += 1
            else:
                character.data['competence_religion'] = True
        elif choi_6_ == 4:
            classe.append('Barde')
            if character.data['competence_investigation'] == True:
                character.data['stat_charisme'] += 1
            else:
                character.data['competence_investigation'] = True
            if character.data['competence_intimidation'] == True:
                character.data['stat_charisme'] += 1
            else:
                character.data['competence_intimidation'] = True
    #  3  +1 Sagesse, compétence : Intuition, Historique : Sage ou Ermite
    elif choi_6 == 3:
        character.data['stat_sagesse'] += 1
        character.data['competence_perception'] = True
        if character.data['competence_histoire'] == True:
            character.data['stat_sagesse'] += 1
        else:
            character.data['competence_histoire'] = True
        historique.append('Sage')
        historique.append('Ermite')
    #  4  +1 Dextérité, compétence : Escamotage, Alignement : Chaotique
    elif choi_6 == 4:
        character.data['stat_dexterity'] += 1
        if character.data['competence_escamotage'] == True:
            character.data['stat_dexterity'] += 1
        else:
            character.data['competence_escamotage'] = True
        historique.append("Voleur")
        classe.append('Roublard')
    #   Question 7 : L’Aventure
    print(
        "Tu peux partir pour une expédition vers un lieu légendaire, mais tu dois tout abandonner. Acceptes-tu ?\n\n",
        "1. Oui, pour découvrir ce lieu interdit.\n",
        "2. Non, j’ai des devoirs ici.\n",
        "3. Oui, mais seulement pour la gloire et la richesse.\n",
        "4. e propose un plan pour organiser l’expédition de manière rentable"
    )
    choi_7 = int(input("Choix (1-4) :\n>>> "))
    #  1   compétence : Survie, historique : Explorateur ou Vagabond
    if choi_7 == 1:
        if character.data['competence_survie'] == True:
            character.data['stat_constitution'] = True
        else:
            character.data['competence_survie'] = True
        historique.append('Explorateur')
        historique.append('Vagabond')
    #  2  Alignement : Loyal, historique : Artisan ou Citadin
    elif choi_7 == 2:
        alignement.append('Loyal Neutre')
        historique.append('Artisan')
        historique.append('Citadin')
        character.data['stat_constitution'] += 1
    #  3   compétence : Persuasion, Alignement : Chaotique Neutre
    elif choi_7 == 3:
        if character.data['competence_persuasion'] == True:
            character.data['stat_charisme'] += 1
        else:
            character.data['competence_persuasion'] = True
        alignement.append('Chaotique Neutre')
    #  4  compétence : Investigation, outils : outils de cartographe
    elif choi_7 == 4:
        if character.data['competence_investigation'] == True:
            character.data['stat_dexterity'] += 1
        else:
            character.data['competence_investigation'] = True
    #   Question 8 : L’Identité
    print(
        "On te prend pour quelqu’un d’autre : un héros ou un criminel célèbre. Que fais-tu ?\n\n",
        "1. Je corrige immédiatement l’erreur.\n",
        "2. Je joue le jeu pour voir ce que j’en retire.\n",
        "3. Je panique et prends la fuite\n",
        "4. Je menace ceux qui m’accusent et retourne la situation."
    )