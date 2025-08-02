# -*- coding: utf-8 -*-
from random import randint
from .class_character import *
from .class_arme import *
from .class_armure import *


def etape_par_etape_RUN():
    character = Character()

    nom = input("Entrez le nom de votre personnage :\n>>> ")
    character.data["name"] = nom

    #       ========= Alignement =========
    print(
        "Dans Donjonet Dragon il existe plusieurs alignements, 9 dans le livre de base :\n",
        "Loyal bon, Loyal neutre, Loyal mauvais, Neutre bon, Neutre, Neutre mauvais,\n",
        "Chaotique bon, Chaotique neutre, Chaotique mauvais."
    )
    alignement = input("Entrez l'alignement de votre personnage :\n>>> ")
    character.data["alignment"] = alignement

    print(
        "Dans Donjonet Dragon il existe plusieurs races, 9 dans le livre de base :\n",
        "Humain, Elfe, Nain, Halfelin, Dragonborn, Tiefling, Gnome, Demi-orc, Demi-elfe.\n",
    )
    check = False
    while check is False:
        race_lst = [
            "Humain", "Elfe", "Nain", "Halfelin", "Dragonborn",
            "Tiefling", "Gnome", "Demi-orc", "Demi-elfe"
        ]
        race = input("Entrez la race de votre personnage :\n>>> ")
        if race in race_lst:
            character.data["race"] = race
            check = True    
    if race == "Humain":
        # toutes les stats principales de character.data passent à 1
        for stat in [
            "stat_force",
            "stat_dexterity",
            "stat_constitution",
            "stat_intelligence",
            "stat_sagesse",
            "stat_charisme"
        ]:
            character.data[stat] = 1
        character.data["vitesse"] = 9
    if race == "Elfe":
        character.data["stat_dexterity"] = 2
        character.data["vitesse"] = 9
        print(
            "Les elfes ont une vitesse de 9 mètres, et un bonus de +2 en dextérité.\n",
            "Ils ont aussi la vision nocturne, et sont résistants aux charmes.")
        print("Il existe plusieurs sous-races d'elfes :\n",
            "Elfe des bois, Elfe des neiges, Elfe noir, Haut-elfe.")
        sous_race = input("Entrez la sous-race de votre elfe :\n>>> ")
        if sous_race == "Elfe des bois":
            character.data["stat_sagesse"] = 1
            print("Les elfes des bois ont un bonus de +1 en sagesse.")
        elif sous_race == "Elfe des neiges":
            character.data["stat_constitution"] = 1
            print("Les elfes des neiges ont un bonus de +1 en constitution.")
        elif sous_race == "Elfe noir":
            character.data["stat_charisme"] = 1
            print("Les elfes noirs ont un bonus de +1 en charisme.")
        elif sous_race == "Haut-elfe":
            character.data["stat_intelligence"] = 1
            print("Les elfes haut-elfes ont un bonus de +1 en intelligence.")
    if race == "Nain":
        character.data["stat_constitution"] = 2
        character.data["vitesse"] = 7.5
        print(
            "Les nains ont une vitesse de 7.5 mètres, et un bonus de +2 en constitution.\n",
            "Ils sont résistants aux poisons et ont une vision nocturne.")
        print("Il existe plusieurs sous-race de nains :\n",
            "Nain des montagnes, Nain des collines, Nain des profondeurs.")
        sous_race = input("Entrez la sous-race de votre nain :\n>>> ")
        if sous_race == "Nain des montagnes":
            character.data["stat_force"] = 1
            print("Les nains des montagnes ont un bonus de +1 en force.")
        elif sous_race == "Nain des collines":
            character.data["stat_sagesse"] = 1
            print("Les nains des collines ont un bonus de +1 en sagesse.")
        elif sous_race == "Nain des profondeurs":
            character.data["stat_charisme"] = 1
            print("Les nains des profondeurs ont un bonus de +1 en charisme.")
    if race == "Halfelin":
        character.data["stat_dexterity"] = 2
        character.data["vitesse"] = 7.5
        print(
            "Les halfelins ont une vitesse de 7.5 mètres, et un bonus de +2 en dextérité.\n",
            "Ils sont chanceux et ont une vision nocturne.")
        print("Il existe plusieurs sous-races de halfelins :\n",
            "Halfelin des champs, Halfelin des collines, Halfelin des profondeurs.")
        sous_race = input("Entrez la sous de votre halfelin :\n>>> ")
        if sous_race == "Halfelin des champs":
            character.data["stat_force"] = 1
            print("Les halfelins des champs ont un bonus de +1 en force.")
        elif sous_race == "Halfelin des collines":
            character.data["stat_sagesse"] = 1
            print("Les halfelins des collines ont un bonus de +1 en sagesse.")
        elif sous_race == "Halfelin des profondeurs":
            character.data["stat_charisme"] = 1
            print("Les halfelins des profondeurs ont un bonus de +1 en charisme.")
    if race == "Dragonborn":
        character.data["stat_force"] = 2
        character.data["vitesse"] = 9
        print(
            "Les dragonborns ont une vitesse de 9 mètres, et un bonus de +2 en force.\n",
            "Ils ont une résistance aux éléments et peuvent cracher du feu.")
        couleur = input("Entrez la couleur de votre dragonborn :\n>>> ")
        if couleur in ["Rouge", "Bleu", "Vert", "Noir", "Blanc"]:
            print(f"Votre dragonborn {couleur} a un bonus de +1 en charisme.")
            character.data["stat_charisme"] = 1
    if race == "Tiefling":
        character.data["stat_charisme"] = 2
        character.data["vitesse"] = 9
        print(
            "Les tieflings ont une vitesse de 9 mètres, et un bonus de +2 en charisme.\n",
            "Ils ont une résistance aux éléments et peuvent lancer des sorts.")
        print("Il existe plusieurs sous-races de tieflings :\n",
            "Tiefling des enfers, Tiefling des abysses, Tiefling des ombres.")
        sous_race = input("Entrez la sous-race de votre tiefling :\n>>> ")
        if sous_race == "Tiefling des enfers":
            character.data["stat_force"] = 1
            print("Les tieflings des enfers ont un bonus de +1 en force.")
        elif sous_race == "Tiefling des abysses":
            character.data["stat_dexterity"] = 1
            print("Les tieflings des abysses ont un bonus de +1 en dextérité.")
        elif sous_race == "Tiefling des ombres":
            character.data["stat_intelligence"] = 1
            print("Les tieflings des ombres ont un bonus de +1 en intelligence.")
    if race == "Gnome":
        character.data["stat_intelligence"] = 2
        character.data["vitesse"] = 7.5
        print(
            "Les gnomes ont une vitesse de 7.5 mètres, et un bonus de +2 en intelligence.\n",
            "Ils sont résistants aux charmes et ont une vision nocturne.")
        print("Il existe plusieurs sous-races de gnomes :\n",
            "Gnome des forêts, Gnome des montagnes, Gnome des profondeurs.")
        sous_race = input("Entrez la sous-race de votre gnome :\n>>> ")
        if sous_race == "Gnome des forêts":
            character.data["stat_dexterity"] = 1
            print("Les gnomes des forêts ont un bonus de +1 en dextérité.")
        elif sous_race == "Gnome des montagnes":
            character.data["stat_constitution"] = 1
            print("Les gnomes des montagnes ont un bonus de +1 en constitution.")
        elif sous_race == "Gnome des profondeurs":
            character.data["stat_charisme"] = 1
            print("Les gnomes des profondeurs ont un bonus de +1 en charisme.")
    if race == "Demi-orc":
        character.data["stat_force"] = 2
        character.data["vitesse"] = 9
        print(
            "Les demi-orcs ont une vitesse de 9 mètres, et un bonus de +2 en force.\n",
            "Ils sont résistants aux poisons et ont une vision nocturne.")
    if race == "Demi-elfe":
        character.data["stat_charisme"] = 2
        character.data["vitesse"] = 9
        print(
            "Les demi-elfes ont une vitesse de 9 mètres, et un bonus de +2 en charisme.\n",
            "Ils sont résistants aux charmes et ont une vision nocturne.")
        print("Ils peuvent choisir deux caractéristiques à augmenter de +1.")
        for stat in ["stat_force", "stat_dexterity", "stat_constitution", 
                     "stat_intelligence", "stat_sagesse"]:
            choice = input(f"Voulez-vous augmenter {stat} de +1 ? (oui/non)\n>>> ")
            if choice.lower() == "oui":
                character.data[stat] += 1
     # caractéristique
    print("Entrez les caractéristiques de votre personnage :\n",
          "En distribuant les valeurs suivantes :\n",
          "15, 14, 13, 12, 10, 8")
    valeur_distribuees = [15, 14, 13, 12, 10, 8]
    
    force = int(input("Entrez la force de votre personnage :\n>>> "))
    while force not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        force = int(input("Entrez la force de votre personnage :\n>>> "))
    valeur_distribuees.remove(force)    
    character.data["stat_force"] = force

    dexterite = int(input("Entrez la dextérité de votre personnage :\n>>> "))
    while dexterite not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        dexterite = int(input("Entrez la dextérité de votre personnage :\n>>> "))
    valeur_distribuees.remove(dexterite)    
    character.data["stat_dexterity"] = dexterite

    constitution = int(input("Entrez la constitution de votre personnage :\n>>> "))
    while constitution not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        constitution = int(input("Entrez la constitution de votre personnage :\n>>> "))
    valeur_distribuees.remove(constitution)    
    character.data["stat_constitution"] = constitution

    intelligence = int(input("Entrez l'intelligence de votre personnage :\n>>> "))
    while intelligence not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        intelligence = int(input("Entrez l'intelligence de votre personnage :\n>>> "))
    valeur_distribuees.remove(intelligence)    
    character.data["stat_intelligence"] = intelligence

    sagesse = int(input("Entrez la sagesse de votre personnage :\n>>> "))
    while sagesse not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        sagesse = int(input("Entrez la sagesse de votre personnage :\n>>> "))
    valeur_distribuees.remove(sagesse)    
    character.data["stat_sagesse"] = sagesse

    charisme = int(input("Entrez le charisme de votre personnage :\n>>> "))
    while charisme not in valeur_distribuees:
        print("Valeur non valide. Veuillez entrer une valeur parmi :", valeur_distribuees)
        charisme = int(input("Entrez le charisme de votre personnage :\n>>> "))
    valeur_distribuees.remove(charisme)    
    character.data["stat_charisme"] = charisme
    
    # classe             
    print(
        "Dans Donjon et Dragon il existe plusieurs classes, 13 dans le livre de base :\n",
        "Barbare, Barde, Clerc, Druide, Guerrier, Moine, Paladin, Rôdeur, Roublard,\n",
        "Ensorceleur, Magicien, Ocultiste.")
    classe = input("Entrez la classe de votre personnage :\n>>> ")
    character.data["class"] = classe
    #       ========== Barbare ==========
    if classe == "Barbare":
        character.data["stat_force"] += 2
        character.data["stat_constitution"] += 1
        character.data["armure"] = 10 + modificateur(character.data["stat_dexterity"])
        character.data["pv_max"] = 12 + modificateur(character.data["stat_constitution"])
        print("Le barbare a un bonus de +2 en force et +1 en constitution.")
        print("Le barbare a une armure de base de 10 + la dextérité.")
        print("Il peut utiliser des armes lourdes et a une grande endurance.")
        print("Le barbare a comme point de vie maximum 12 + la constitution.")
        print("Il peut choisir deux compétences parmi :\n",
            "Dressage d'animaux, Athlétisme, Intimidation, Nature, Perception et Survi.")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")    
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "dressage d'animaux":
                character.data["competence_dressage_animaux"] = True
            elif competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "nature":
                character.data["competence_nature"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "survie":
                character.data["competence_survie"] = True
    #       ========== Barde ==========
    elif classe == "Barde":
        character.data["stat_charisme"] += 2
        character.data["stat_dexterity"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        print("Le barde a un bonus de +2 en charisme et +1 en dextérité.")
        print("Le barde a comme point de vie maximum 8 + la constitution.")
        print("Le barde a accès à la magie et peut utiliser des instruments de musique.")
        print("Il peut choisir trois compétences parmi :\n",
            "Acrobatie, Arcanes, Athlétisme, Discrétion, Histoire,\n",
            "Intimidation, Investigation, Médecine, Nature,\n",
            "Perception, Persuasion, Religion, Survie, Tromperie.") 
        competences = input(
            "Choisissez trois compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "acrobatie":
                character.data["competence_acrobatie"] = True
            elif competence == "arcanes":
                character.data["competence_arcanes"] = True
            elif competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "discrétion":
                character.data["competence_discretion"] = True
            elif competence == "histoire":
                character.data["competence_histoire"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "investigation":
                character.data["competence_investigation"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "nature":
                character.data["competence_nature"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "persuasion":
                character.data["competence_persuasion"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
            elif competence == "survie":
                character.data["competence_survie"] = True
            elif competence == "tromperie":
                character.data["competence_tromperie"] = True
        print("Le barde porte une armure légère. Il en existe plusieurs types :\n",
            "Matelassée, Armure de cuir clouté, Cuir")
        armure = input("Entrez le type d'armure de votre barde :\n>>> ")
        if armure == "Matelassée":
            character.data['armure_type'] = "Matelassée"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Armure de cuir clouté":
            character.data['armure_type'] = "Armure de cuir clouté"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Armure de cuir clouté", "data/base/item/armure.txt").data['armor_class'] )   
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        print("Le barde peut utiliser des armes simples et des armes de guerre.")
    #       ========== Clerc ==========
    elif classe == "Clerc":
        character.data["stat_sagesse"] += 2
        character.data["stat_charisme"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        print("Le clerc a un bonus de +2 en sagesse et +1 en charisme.")
        print("Le clerc a comme point de vie maximum 8 + la constitution.")
        print("Le clerc a accès à la magie divine et peut utiliser des armes et armures.")
        print("Il peut choisir deux compétences parmi :\n",
             "Histoire, Perspicacité, Médecine, Persuasion et Religion")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "histoire":
                character.data["competence_histoire"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "persuasion":
                character.data["competence_persuasion"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
        print("Le clerc porte une armure légère ou intermédiaire. Il en existe plusieurs types :\n",
            "Pour les légère : Cuir clouté, Cuir, Matelassé\n",
            "Pour les intermédiaires : Peaux, Chemise de mailles, Écailles, Cuirasse, Demi-plate")
        armure = input("Entrez le type d'armure de votre clerc :\n>>> ")
        if armure == "Cuir clouté":
            character.data['armure_type'] = "Cuir cloute"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Matelassee":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Peaux":
            character.data['armure_type'] = "Peaux"
            character.data["armure"] = modificateur(character.data["stat_dexterity"])  + int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Chemise de mailles":
            character.data['armure_type'] = "Chemise de mailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"])  + int(armure_get_by_name("Chemise de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Écailles":
            character.data['armure_type'] = "Ecailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Ecailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuirasse":
            character.data['armure_type'] = "Cuirasse"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Demi-plate":
            character.data['armure_type'] = "Demi-plate"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Demi-plate", "data/base/item/armure.txt").data['armor_class'])
        print("Le clerc peut utiliser des armes simples et des armes de guerre.")
    #       ========== Druide ==========
    elif classe == "Druide":
        character.data["stat_sagesse"] += 2
        character.data["stat_dexterity"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        print("Le druide a un bonus de +2 en sagesse et +1 en dextérité.")
        print("Le druide a accès à la magie naturelle et peut utiliser des armes simples.")
        print("Il peut choisir deux compétences parmi :\n", 
            "Arcanes, Perspicacité, Médecine, Nature, Perception, Religion et Survie")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "arcanes":
                character.data["competence_arcanes"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "nature":
                character.data["competence_nature"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
            elif competence == "survie":
                character.data["competence_survie"] = True
        print("Le druide porte une armure légère ou intermédiaire. Il en existe plusieurs types :\n",
            "Pour les légère : Cuir clouté, Cuir, Matelassé\n",
            "Pour les intermédiaires : Peaux, Chemise de mailles, Écailles, Cuirasse, Demi-plate")
        armure = input("Entrez le type d'armure de votre druide :\n>>> ")
        if armure == "Cuir clouté":
            character.data['armure_type'] = "Cuir cloute"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])   
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Matelassee":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Peaux":
            character.data['armure_type'] = "Peaux"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Chemise de mailles":
            character.data['armure_type'] = "Chemise de mailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Chemise de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Ecailles":
            character.data['armure_type'] = "Ecailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Ecailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuirasse":
            character.data['armure_type'] = "Cuirasse"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Demi-plate":
            character.data['armure_type'] = "Demi-plate"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Demi-plate", "data/base/item/armure.txt").data['armor_class'])

    #      ========== Guerrier ==========
    elif classe == "Guerrier":
        character.data["stat_force"] += 2
        character.data["stat_constitution"] += 1
        character.data["pv_max"] = 10 + modificateur(character.data["stat_constitution"])
        print("Le guerrier a un bonus de +2 en force et +1 en constitution.")
        print("Le guerrier a accès à la magie martiale et peut utiliser des armes et armures.")
        print("Il peut choisir deux compétences parmi :\n",
            "Athlétisme,Acrobaties , Intimidation, Perception, Survie, Médecine et Histoire")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "acrobaties":
                character.data["competence_acrobatie"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "survie":
                character.data["competence_survie"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "histoire":
                character.data["competence_histoire"] = True
        print("Le guerrier porte une armure légère, intermédiaire ou lourde. Il en existe plusieurs types :\n",
            "Pour les légère : Cuir clouté, Cuir, Matelassé\n",
            "Pour les intermédiaires : Peaux, Chemise de mailles, Écailles, Cuirasse, Demi-plate\n",
            "Pour les lourdes : Broigne, Cotte de mailles, Clibanion et Harnois")
        armure = input("Entrez le type d'armure de votre guerrier :\n>>> ")
        if armure == "Cuir clouté":
            character.data['armure_type'] = "Cuir cloute"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Matelassee":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Peaux":
            character.data['armure_type'] = "Peaux"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Chemise de mailles":
            character.data['armure_type'] = "Chemise de mailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Chemise de mailles", "data/base/item/armure.txt").data['armor_class'])    
        elif armure == "Ecailles":
            character.data['armure_type'] = "Ecailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Ecailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuirasse":
            character.data['armure_type'] = "Cuirasse"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Demi-plate":
            character.data['armure_type'] = "Demi-plate"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Demi-plate", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Broigne":
            character.data['armure_type'] = "Broigne"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Broigne", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cotte de mailles":
            character.data['armure_type'] = "Cotte de mailles"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cotte de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Clibanion":
            character.data['armure_type'] = "Clibanion"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Clibanion", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Harnois":
            character.data['armure_type'] = "Harnois"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Harnois", "data/base/item/armure.txt").data['armor_class'])
        print("Le guerrier peut utiliser des armes simples et des armes de guerre.")
    #       ========== Moine ==========
    elif classe == "Moine":
        character.data["stat_dexterity"] += 2
        character.data["stat_sagesse"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        print("Le moine a un bonus de +2 en dextérité et +1 en sagesse.")
        print("Le moine a accès à la magie martiale et peut utiliser des armes simples.")
        print("Il peut choisir deux compétences parmi :\n",
            "Acrobaties, Athlétisme, Histoire, Perspicacité, Religion et Furtivité")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "acrobaties":
                character.data["competence_acrobatie"] = True
            elif competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "histoire":
                character.data["competence_histoire"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
            elif competence == "furtivité":
                character.data["competence_furtivite"] = True
        print("Le moine ne porte pas d'armure, mais peut utiliser des armes simples.")
        character.data["armure"] = 10 + character.data["stat_dexterity"]
    #       ========== Paladin ==========
    elif classe == "Paladin":
        character.data["stat_force"] += 2
        character.data["stat_charisme"] += 1
        character.data["pv_max"] = 10 + modificateur(character.data["stat_constitution"])
        print("Le paladin a un bonus de +2 en force et +1 en charisme.")
        print("Le paladin a accès à la magie divine et peut utiliser des armes et armures.")
        print("Il peut choisir deux compétences parmi :\n",
            "Athlétisme, Perspicacité, Intimidation, Médecine, Persuasion et Religion")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "persuasion":
                character.data["competence_persuasion"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
        print("Le paladin porte une armure légère, intermédiaire ou lourde. Il en existe plusieurs types :\n", 
            "Pour les légère : Cuir clouté, Cuir, Matelassé\n",
            "Pour les intermédiaires : Peaux, Chemise de mailles, Écailles, Cuirasse, Demi-plate\n",
            "Pour les lourdes : Broigne, Cotte de mailles, Clibanion et Harnois")   
        armure = input("Entrez le type d'armure de votre paladin :\n>>> ")
        if armure == "Cuir clouté":
            character.data['armure_type'] = "Cuir cloute"
            character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Matelassee":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Peaux":
            character.data['armure_type'] = "Peaux"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Chemise de mailles":
            character.data['armure_type'] = "Chemise de mailles"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Chemise de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Ecailles":
            character.data['armure_type'] = "Ecailles"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Ecailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuirasse":
            character.data['armure_type'] = "Cuirasse"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Demi-plate":
            character.data['armure_type'] = "Demi-plate"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Demi-plate", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Broigne":
            character.data['armure_type'] = "Broigne"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Broigne", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cotte de mailles":
            character.data['armure_type'] = "Cotte de mailles"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cotte de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Clibanion":
            character.data['armure_type'] = "Clibanion"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Clibanion", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Harnois":
            character.data['armure_type'] = "Harnois"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Harnois", "data/base/item/armure.txt").data['armor_class'])

    #       ========== Rôdeur ==========
    elif classe == "Rôdeur":
        character.data["stat_dexterity"] += 2
        character.data["stat_sagesse"] += 1
        character.data["pv_max"] = 10 + modificateur(character.data["stat_constitution"])
        print("Le rôdeur a un bonus de +2 en dextérité et +1 en sagesse.")
        print("Le rôdeur a accès à la magie naturelle et peut utiliser des armes et armures.")
        print("Il peut choisir deux compétences parmi :\n",
            "Athlétisme, Perspicacité, Investigation, Nature, Perception, Discrétion et Survie")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "investigation":
                character.data["competence_investigation"] = True
            elif competence == "nature":
                character.data["competence_nature"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "discrétion":
                character.data["competence_discretion"] = True
            elif competence == "survie":
                character.data["competence_survie"] = True
        print("Le rôdeur porte une armure légère ou intermédiaire. Il en existe plusieurs types :\n",
            "Pour les légère : Cuir clouté, Cuir, Matelassé\n",
            "Pour les intermédiaires : Peaux, Chemise de mailles, Écailles, Cuirasse, Demi-plate")
        armure = input("Entrez le type d'armure de votre rôdeur :\n>>> ")
        if armure == "Cuir clouté":
            character.data['armure_type'] = "Cuir cloute"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Matelassee":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Peaux":
            character.data['armure_type'] = "Peaux"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Chemise de mailles":
            character.data['armure_type'] = "Chemise de mailles"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Chemise de mailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Ecailles":
            character.data['armure_type'] = "Ecailles"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Ecailles", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuirasse":
            character.data['armure_type'] = "Cuirasse"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Demi-plate":
            character.data['armure_type'] = "Demi-plate"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Demi-plate", "data/base/item/armure.txt").data['armor_class'])
    #       ========== Roublard ==========
    elif classe == "Roublard":
        character.data["stat_dexterity"] += 2
        character.data["stat_charisme"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        print("Le roublard a un bonus de +2 en dextérité et +1 en charisme.")
        print("Le roublard a accès à la magie martiale et peut utiliser des armes simples.")
        print("Il peut choisir trois compétences parmi :\n",
            " Acrobaties, Athlétisme, Tromperie, Perspicacité, Intimidation, Investigation, Perception, Performance et Persuasion")
        competences = input(
            "Choisissez trois compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")    
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "acrobaties":
                character.data["competence_acrobatie"] = True
            elif competence == "athlétisme":
                character.data["competence_athletisme"] = True
            elif competence == "tromperie":
                character.data["competence_tromperie"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "investigation":
                character.data["competence_investigation"] = True
            elif competence == "perception":
                character.data["competence_perception"] = True
            elif competence == "performance":
                character.data["competence_performance"] = True
            elif competence == "persuasion":
                character.data["competence_persuasion"] = True
        print("Le roublard porte une armure légère. Il en existe plusieurs types :\n", 
            "Matelassée, Armure de cuir clouté, Cuir")
        armure = input("Entrez le type d'armure de votre roublard :\n>>> ")
        if armure == "Matelassée":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Armure de cuir clouté":
            character.data['armure_type'] = "Cuir Cloute"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir Cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    #       ========== Magicien ==========
    elif classe == "Magicien":
        character.data["stat_intelligence"] += 2
        character.data["stat_charisme"] += 1
        character.data["pv_max"] = 6 + modificateur(character.data["stat_constitution"])
        print("Le magicien a un bonus de +2 en intelligence et +1 en charisme.")
        print("Le sorcmagicienier a accès à la magie arcanique et peut utiliser des armes simples.")
        print("Il peut choisir deux compétences parmi :\n",
            "Arcanes, Histoire, Perspicacité, Investigation, Médecine et Religion")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "arcanes":
                character.data["competence_arcanes"] = True
            elif competence == "histoire":
                character.data["competence_histoire"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "investigation":
                character.data["competence_investigation"] = True
            elif competence == "médecine":
                character.data["competence_medic"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
        print("Le magicien porte une armure légère. Il en existe plusieurs types :\n",
            "Matelassée, Armure de cuir clouté, Cuir")
        armure = input("Entrez le type d'armure de votre magicien :\n>>> ")
        if armure == "Matelassée":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Armure de cuir clouté":
            character.data['armure_type'] = "Cuir Cloute"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir Cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
        print("Le magicien peut utiliser des armes simples.")
    #       ========== Ensorceleur ==========
    elif classe == "Ensorceleur":
        character.data["stat_charisme"] += 2
        character.data["stat_dexterity"] += 1
        character.data["pv_max"] = 6 + modificateur(character.data["stat_constitution"])
        print("L'ensorceleur a un bonus de +2 en charisme et +1 en dextérité.")
        print("L'ensorceleur a accès à la magie arcanique et peut utiliser des armes simples.")
        print("Il peut choisir deux compétences parmi :\n",
            "Arcanes, Tromperie, Perspicacité, Intimidation, Persuasion et Religion")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "arcanes":
                character.data["competence_arcanes"] = True
            elif competence == "tromperie":
                character.data["competence_tromperie"] = True
            elif competence == "perspicacité":
                character.data["competence_perception"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "persuasion":
                character.data["competence_persuasion"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
        print("L'ensorceleur porte une armure légère. Il en existe plusieurs types :\n",
            "Matelassée, Armure de cuir clouté, Cuir")
        armure = input("Entrez le type d'armure de votre ensorceleur :\n>>> ")
        if armure == "Matelassée":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Armure de cuir clouté":
            character.data['armure_type'] = "Cuir Cloute"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir Cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    #       ========== Ocultiste ==========
    elif classe == "Ocultiste":
        character.data["stat_intelligence"] += 2
        character.data["stat_charisme"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])  
        print("L'ocultiste a un bonus de +2 en intelligence et +1 en charisme.")
        print("L'ocultiste a accès à la magie arcanique et peut utiliser des armes simples.")
        print("Il peut choisir deux compétences parmi :\n",
            "Arcanes, Tromperie, Histoire, Intimidation, Investigation, Nature et Religion")
        competences = input(
            "Choisissez deux compétences parmi celles proposées, séparées par une virgule :\n>>> "
        ).split(",")
        for competence in competences:
            competence = competence.strip().lower()
            if competence == "arcanes":
                character.data["competence_arcanes"] = True
            elif competence == "tromperie":
                character.data["competence_tromperie"] = True
            elif competence == "histoire":
                character.data["competence_histoire"] = True
            elif competence == "intimidation":
                character.data["competence_intimidation"] = True
            elif competence == "investigation":
                character.data["competence_investigation"] = True
            elif competence == "nature":
                character.data["competence_nature"] = True
            elif competence == "religion":
                character.data["competence_religion"] = True
        
        print("L'ocultiste porte une armure légère. Il en existe plusieurs types :\n",
            "Matelassée, Armure de cuir clouté, Cuir")
        armure = input("Entrez le type d'armure de votre occultiste :\n>>> ")
        if armure == "Matelassée":
            character.data['armure_type'] = "Matelassee"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Armure de cuir clouté":
            character.data['armure_type'] = "Cuir Cloute"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir Cloute", "data/base/item/armure.txt").data['armor_class'])
        elif armure == "Cuir":
            character.data['armure_type'] = "Cuir"
            character.data["armure"] =modificateur(character.data["stat_dexterity"])+ int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])



    niveau = int(input("Entrez le niveau de votre personnage :\n>>> "))
    character.data["niveau"] = niveau

   
    
    character.data["pv"] = character.data["pv_max"]

    print(
        "Vous avez fini de créer votre personnage ! Voici sa fiche\n",
        "================================================================\n",
        character
    )
    valider = input("Voulez-vous valider la création de votre personnage ? (oui/non)\n>>> ").strip().lower()
    if valider != "oui":
        print("Création annulée.")
        return False
    character.save(f"data/save/character/{character.data['name']}.txt")
    return True

if __name__ == "__main__":
    etape_par_etape_RUN() 