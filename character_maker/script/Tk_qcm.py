# -*- coding: utf-8 -*-
from random import randint
from .class_character import *
from .class_arme import *
from .class_armure import *

import tkinter as tk
from tkinter import simpledialog, messagebox

def ask_string(title, question):
    root = tk.Tk()
    root.withdraw()
    answer = simpledialog.askstring(title, question)
    root.destroy()
    return answer

def ask_int(title, question, minval=1, maxval=99):
    root = tk.Tk()
    root.withdraw()
    answer = simpledialog.askinteger(title, question, minvalue=minval, maxvalue=maxval)
    root.destroy()
    return answer

def ask_choice(title, question, choices):
    root = tk.Tk()
    root.withdraw()
    answer = simpledialog.askinteger(
        title,
        question + "\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(choices)]),
        minvalue=1,
        maxvalue=len(choices)
    )
    root.destroy()
    return answer

def show_result(title, character, outils):
    # Affiche le résumé du personnage dans une fenêtre Tkinter avec plusieurs colonnes
    root = tk.Tk()
    root.title(title)
    root.geometry("900x500")
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Prépare les données à afficher
    infos = [
        ("Nom", character.data["name"]),
        ("Race", character.data["race"]),
        ("Classe", character.data["classe"]),
        ("Niveau", character.data["level"]),
        ("Alignement", character.data["alignment"]),
        ("Historique", character.data["historique"]),
        ("Outils", ", ".join(str(o) for o in outils)),
        ("PV", character.data.get("pv", "")),
        ("PV max", character.data.get("pv_max", "")),
        ("Armure", character.data.get("armure", "")),
        ("Type armure", character.data.get("armure_type", "")),
    ]
    stats = [(k.replace("stat_", "").capitalize(), v) for k, v in character.data.items() if k.startswith("stat_")]
    competences = [(k.replace("competence_", "").capitalize(), "Oui") for k, v in character.data.items() if k.startswith("competence_") and v]
    sauvegardes = [(k.replace("sauvegarde_", "").capitalize(), v) for k, v in character.data.items() if k.startswith("sauvegarde_") and v > 0]

    # Affichage en colonnes
    columns = [
        ("Informations", infos),
        ("Statistiques", stats),
        ("Compétences", competences),
        ("Sauvegardes", sauvegardes)
    ]

    for col, (title_col, data) in enumerate(columns):
        col_frame = tk.LabelFrame(frame, text=title_col, padx=10, pady=10)
        col_frame.grid(row=0, column=col, sticky="n")
        for i, (label, value) in enumerate(data):
            tk.Label(col_frame, text=f"{label} : {value}", anchor="w").grid(row=i, column=0, sticky="w")

    # Bouton pour fermer
    tk.Button(root, text="Fermer", command=root.destroy).pack(pady=10)
    root.mainloop()

def qcm():
    character = Character()
    classe = []
    alignement = []
    historique = []
    race = []
    competance = []
    outils = []

    character.data["name"] = ask_string("Nom", "Quel est le nom de votre personnage ?")
    character.data["level"] = ask_int("Niveau", "Quel est le niveau de votre personnage ?", 1, 20)

    # Question 1
    choi_1 = ask_choice(
        "Question 1 : L’Enfance",
        "Tu es un enfant dans un village isolé. Un étranger blessé arrive en titubant à la tombée de la nuit. Il demande de l'aide. Que fais-tu ?",
        [
            "Je cours chercher un adulte.",
            "Je le soigne moi-même avec ce que je trouve.",
            "Je le fouille discrètement pour voir s’il a quelque chose d'intéressant.",
            "Je le menace de s'éloigner : il pourrait être dangereux."
        ]
    )
    if choi_1 == 1:
        character.data["stat_sagesse"] += 1
        historique.append("Villageois")
        historique.append("Acolyte")
    elif choi_1 == 2:
        character.data["stat_intelligence"] += 1
        character.data["competence_medic"] = True
    elif choi_1 == 3:
        character.data["stat_dexterity"] += 1
        character.data["alignment"] = "Chaotique Neutre"
        historique.append("Voleur")
        character.data['competence_escamotage'] = True
        classe.append('Roublard')
    elif choi_1 == 4:
        character.data["stat_force"] += 2
        alignement.append("Loyal Neutre")
        alignement.append("Loyal Mauvais")

    # Question 2
    choi_2 = ask_choice(
        "Question 2 : Le Conflit",
        "Une bande de brigands menace ton village. Tu es assez jeune mais motivé à agir. Quelle est ta réponse ?",
        [
            "J'organise la défense avec les anciens et les chasseurs.",
            "Je prépare un piège dans les bois, sans en parler à personne.",
            "Je propose de négocier avec les brigands.",
            "Je m'enfuis discrètement la nuit avec mes proches."
        ]
    )
    if choi_2 == 1:
        classe.append("Paladin")
        classe.append("Guerrier")
        alignement.append("Loyal Bon")
        character.data["stat_constitution"] += 2
    elif choi_2 == 2:
        classe.append("Rôdeur")
        classe.append("Voleur")
        alignement.append("Neutre")
        character.data["stat_dexterity"] += 1
        character.data["competence_survie"] = True
    elif choi_2 == 3:
        character.data["stat_charisme"] += 1
        classe.append("Barde")
        classe.append("Ensorceleur")
        character.data["competence_tromperie"] = True
    elif choi_2 == 4:
        historique.append("Réfugié")
        alignement.append("Neutre Bon")
        character.data["competence_survie"] = True
        character.data["stat_sagesse"] += 1

    # Question 3
    choi_3 = ask_choice(
        "Question 3 : La Découverte",
        "Tu tombes par hasard sur un ancien livre couvert de symboles étranges. Que fais-tu ?",
        [
            "Je l'étudie, fasciné",
            "Je le cache pour le vendre plus tard",
            "Je le brûle, par peur de la magie.",
            "Je le remets à une autorité religieuse."
        ]
    )
    if choi_3 == 1:
        character.data["stat_intelligence"] += 1
        classe.append("Magicien")
        character.data['competence_arcanes'] = True
    elif choi_3 == 2:
        character.data["stat_intelligence"] += 1
        character.data["stat_dexterity"] += 1
        alignement.append('Chaotique Neutre')
    elif choi_3 == 3:
        alignement.append("Loyal Neutre")
        alignement.append("Loyal Bon")
        race.append("Naine")
        race.append('Demi-orque')
        classe.append('Barbare')
        character.data["stat_force"] += 2
    elif choi_3 == 4:
        historique.append("Acolyte")
        classe.append("Clerc")
        alignement.append("Loyal Bon")
        character.data["competence_religion"] = True
        character.data['stat_sagesse'] += 1

    # Question 4
    choi_4 = ask_choice(
        "Question 4 : La Trahison",
        "Un ami d’enfance trahit ton groupe et rejoint un seigneur ennemi. Quelle est ta réaction ?",
        [
            "Je pars à sa recherche pour comprendre son choix.",
            "Je jure de le tuer pour sa trahison.",
            "Je laisse faire, cela ne me concerne pas.",
            "Je tente de le convaincre de revenir."
        ]
    )
    if choi_4 == 1:
        character.data["stat_charisme"] += 1
        historique.append("Noble")
        historique.append("Héros du peuple")
        classe.append("Paladin")
        character.data["stat_charisme"] += 1
        character.data['competence_investigation'] = True
    elif choi_4 == 2:
        alignement.append("Neutre")
        alignement.append("Mauvais")
        classe.append("Guerrier")
        classe.append("Barbare")
        character.data["sauvegarde_force"] += 1
        race.append("Demi-orque")
    elif choi_4 == 3:
        alignement.append('Neutre')
        race.append('Humain')
        character.data['stat_constitution'] += 1
    elif choi_4 == 4:
        character.data["stat_charisme"] += 1
        classe.append('Classe')
        classe.append('Clerc')
        character.data['competence_persuasion'] = True

    # Question 5
    choi_5 = ask_choice(
        "Question 5 : Le Sang",
        "On t’annonce que tu es issu d’un peuple ancien, aux pouvoirs étranges. Quelle est ta réaction ?",
        [
            "J’embrasse cet héritage",
            "Je nie cette vérité, préférant mon identité actuelle.",
            "Je l’utilise à mon avantage.",
            "Je pars à la recherche d’autres comme moi."
        ]
    )
    if choi_5 == 1:
        if 'Humain' in race:
            race.append('Demi-elfe')
        elif character.data['sauvegarde_constitution'] >= 3:
            race.append('Drakéide')
        else:
            race.append('Tieffelin')
        character.data["stat_sagesse"] += 1
    elif choi_5 == 2:
        alignement.append('Loyal')
        race.append('Humain')
        race.append('Demi-orque')
        race.append('Nain')
    elif choi_5 == 3:
        alignement.append('Chaotique')
        classe.append('Occultiste')
    elif choi_5 == 4:
        historique.append('Sage')
        historique.append('Ermite')

    # Question 6
    choi_6 = ask_choice(
        "Question 6 : Le Savoir",
        "Un vieux professeur te propose de t’enseigner tout ce qu’il sait, mais il ne reste qu’un mois à vivre. Que fais-tu ?",
        [
            "J’étudie sans relâche, quitte à m’épuiser.",
            "Je choisis un sujet qui me passionne et me concentre dessus.",
            "Je passe du temps avec lui à échanger sur la vie.",
            "Je vole ses notes et pars. Je n’ai pas le temps d’attendre."
        ]
    )
    if choi_6 == 1:
        outils.append('Outils de calligraphie')
        character.data['stat_intelligence'] += 1
        if character.data['competence_arcanes'] == True:
            character.data['stat_intelligence'] += 1
        else:
            character.data['competence_arcanes'] = True
        classe.append('Magicien')
    elif choi_6 == 2:
        character.data['stat_intelligence'] += 1
        choi_6_ = ask_choice(
            "Choix de savoir",
            "Vous avez le choix entre :",
            [
                "Les savoirs et arts de la nature",
                "Les histoire du passé",
                "Les forces qui érige ce monde",
                "Les savoires interdit de sciences social"
            ]
        )
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
    elif choi_6 == 3:
        character.data['stat_sagesse'] += 1
        character.data['competence_perception'] = True
        if character.data['competence_histoire'] == True:
            character.data['stat_sagesse'] += 1
        else:
            character.data['competence_histoire'] = True
        historique.append('Sage')
        historique.append('Ermite')
    elif choi_6 == 4:
        character.data['stat_dexterity'] += 1
        if character.data['competence_escamotage'] == True:
            character.data['stat_dexterity'] += 1
        else:
            character.data['competence_escamotage'] = True
        historique.append("Voleur")
        classe.append('Roublard')

    # Question 7
    choi_7 = ask_choice(
        "Question 7 : L’Aventure",
        "Tu peux partir pour une expédition vers un lieu légendaire, mais tu dois tout abandonner. Acceptes-tu ?",
        [
            "Oui, pour découvrir ce lieu interdit.",
            "Non, j’ai des devoirs ici.",
            "Oui, mais seulement pour la gloire et la richesse.",
            "Je propose un plan pour organiser l’expédition de manière rentable"
        ]
    )
    if choi_7 == 1:
        if character.data['competence_survie'] == True:
            character.data['stat_constitution'] += 1
        else:
            character.data['competence_survie'] = True
        historique.append('Explorateur')
        historique.append('Vagabond')
    elif choi_7 == 2:
        alignement.append('Loyal Neutre')
        historique.append('Artisan')
        historique.append('Citadin')
        character.data['stat_constitution'] += 2
    elif choi_7 == 3:
        if character.data['competence_persuasion'] == True:
            character.data['stat_charisme'] += 1
        else:
            character.data['competence_persuasion'] = True
        alignement.append('Chaotique Neutre')
    elif choi_7 == 4:
        outils.append('Outils de cartographe')
        if character.data['competence_investigation'] == True:
            character.data['stat_dexterity'] += 1
        else:
            character.data['competence_investigation'] = True

    # Question 8
    choi_8 = ask_choice(
        "Question 8 : L’Artisanat",
        "Quel type d’activité manuelle te rend le plus fier ?",
        [
            "La forge ou la menuiserie.",
            "La cuisine ou la médecine.",
            "La peinture ou la musique.",
            "Je n’aime pas me salir les mains."
        ]
    )
    if choi_8 == 1:
        competance.append('Artisanat')
        outils.append('Outils de forgeron')
        race.append('Nain')
        character.data['stat_force'] += 2
        character.data['stat_constitution'] += 1
    elif choi_8 == 2:
        outils.append('Ustensiles de cuisinier')
        outils.append("Ustensiles d'herboriste")
        if character.data['competence_medic'] == True:
            character.data['stat_intelligence'] += 1
        else:
            character.data['competence_medic'] = True
        race.append('Humain')
        race.append('Demi-elfe')
        race.append('Elfe')
        classe.append('Druide')
    elif choi_8 == 3:
        choi_8_ = ask_choice(
            "Musique ou Peinture",
            "Plus musique ou peinture ?",
            ["Musique", "Peinture"]
        )
        classe.append('Barde')
        if choi_8_ == 1:
            outils.append('Instrument de musique')
            if character.data['competence_representation'] == True:
                character.data['stat_charisme'] += 1
            else:
                character.data['competence_representation'] = True
        elif choi_8_ == 2:
            outils.append('Outils de peintre')
            if character.data['competence_representation'] == True:
                character.data['stat_sagesse'] += 1
            else:
                character.data['competence_representation'] = True
    elif choi_8 == 4:
        character.data['stat_charisme'] += 1
        race.append('Elfe')
        race.append('Tieffelin')

    # Question 9
    choi_9 = ask_choice(
        "Question 9 : Le Mystère",
        "Une étrange entité t’offre un pouvoir en échange d’un service futur inconnu. Acceptes-tu ?",
        [
            "Oui, le pouvoir m’aidera à faire le bien.",
            "Non, je refuse tout pacte sans condition.",
            "Oui, mais je prépare un plan pour trahir l’entité.",
            "Je tente de piéger ou détruire l’entité."
        ]
    )
    if choi_9 == 1:
        classe.append('Occultiste')
        alignement.append('Loyal Bon')
        alignement.append('Neutre Bon')
    elif choi_9 == 2:
        alignement.append('Loyal Bon')
        alignement.append('Loyal Mauvais')
        character.data['stat_sagesse'] += 1
        classe.append('Paladin')
        classe.append('Clerc')
    elif choi_9 == 3:
        alignement.append('Chaotique Neutre')
        if character.data['competence_tromperie'] == True:
            character.data['stat_charisme'] += 1
        else:
            character.data['competence_tromperie'] = True
        character.data['stat_intelligence'] += 1
    elif choi_9 == 4:
        classe.append('Paladin')
        classe.append('Clerc')
        classe.append('Roublard')

    # Calculs finaux
    if len(race) > 0:
        race_max = max(set(race), key=race.count)
    else:
        race_max = "Humain"
    character.data['race'] = race_max

    if len(alignement) > 0:
        alignement_max = max(set(alignement), key=alignement.count)
    else:
        alignement_max = "Neutre"
    character.data['alignment'] = alignement_max

    if len(historique) > 0:
        historique_max = max(set(historique), key=historique.count)
    else:
        historique_max = "Aucun"
    character.data['historique'] = historique_max

    if len(competance) > 0:
        competance_max = max(set(competance), key=competance.count)
    else:
        competance_max = "Aucune"
    character.data['competence'] = competance_max

    # Classe
    if character.data['stat_force'] >= character.data['stat_dexterity'] and character.data['stat_force'] >= character.data['stat_constitution'] and character.data['stat_force'] >= character.data['stat_intelligence'] and character.data['stat_force'] >= character.data['stat_sagesse'] and character.data['stat_force'] >= character.data['stat_charisme']:
        classe.append('Guerrier')
        classe.append('Barbare')
    elif character.data['stat_dexterity'] >= character.data['stat_force'] and character.data['stat_dexterity'] >= character.data['stat_constitution'] and character.data['stat_dexterity'] >= character.data['stat_intelligence'] and character.data['stat_dexterity'] >= character.data['stat_sagesse'] and character.data['stat_dexterity'] >= character.data['stat_charisme']:
        classe.append('Voleur')
        classe.append('Rodeur')
    elif character.data['stat_constitution'] >= character.data['stat_force'] and character.data['stat_constitution'] >= character.data['stat_dexterity'] and character.data['stat_constitution'] >= character.data['stat_intelligence'] and character.data['stat_constitution'] >= character.data['stat_sagesse'] and character.data['stat_constitution'] >= character.data['stat_charisme']:
        classe.append('Guerrier')
        classe.append('Paladin')
        if character.data['competence_religion'] == True:
            classe.append('Clerc')
    elif character.data['stat_intelligence'] >= character.data['stat_force'] and character.data['stat_intelligence'] >= character.data['stat_dexterity'] and character.data['stat_intelligence'] >= character.data['stat_constitution'] and character.data['stat_intelligence'] >= character.data['stat_sagesse'] and character.data['stat_intelligence'] >= character.data['stat_charisme']:
        classe.append('Magicien')
        classe.append('Occultiste')
        classe.append('Ensorceleur')
    elif character.data['stat_sagesse'] >= character.data['stat_force'] and character.data['stat_sagesse'] >= character.data['stat_dexterity'] and character.data['stat_sagesse'] >= character.data['stat_constitution'] and character.data['stat_sagesse'] >= character.data['stat_intelligence'] and character.data['stat_sagesse'] >= character.data['stat_charisme']:
        classe.append('Druide')
        if character.data['competence_religion'] == True:
            classe.append('Clerc')
    elif character.data['stat_charisme'] >= character.data['stat_force'] and character.data['stat_charisme'] >= character.data['stat_dexterity'] and character.data['stat_charisme'] >= character.data['stat_constitution'] and character.data['stat_charisme'] >= character.data['stat_intelligence'] and character.data['stat_charisme'] >= character.data['stat_sagesse']:
        classe.append('Barde')
        classe.append('Ensorceleur')
        classe.append('Paladin')
    classe_max = max(set(classe), key=classe.count)
    character.data['classe'] = classe_max

    # Ajustement des stats
    for stat in ['stat_force', 'stat_dexterity', 'stat_constitution', 'stat_intelligence', 'stat_sagesse', 'stat_charisme']:
        if character.data[stat] > 17:
            character.data[stat] = 17

    total_stat = sum([character.data[s] for s in ['stat_force', 'stat_dexterity', 'stat_constitution', 'stat_intelligence', 'stat_sagesse', 'stat_charisme']])
    if total_stat < 72:
        diff = 72 - total_stat
        stats = [randint(1, 6) for _ in range(6)]
        while sum(stats) < diff:
            stats[randint(0, 5)] += 1
        for i, stat in enumerate(['stat_force', 'stat_dexterity', 'stat_constitution', 'stat_intelligence', 'stat_sagesse', 'stat_charisme']):
            character.data[stat] += stats[i]
    elif total_stat > 72:
        diff = total_stat - 72
        stats = [character.data[s] for s in ['stat_force', 'stat_dexterity', 'stat_constitution', 'stat_intelligence', 'stat_sagesse', 'stat_charisme']]
        while sum(stats) > 72:
            index = stats.index(max(stats))
            stats[index] -= 1
        for i, stat in enumerate(['stat_force', 'stat_dexterity', 'stat_constitution', 'stat_intelligence', 'stat_sagesse', 'stat_charisme']):
            character.data[stat] = stats[i]

    # PV et armure selon la classe
    if classe_max == 'Barbare':
        character.data['pv_max'] = 12 + modificateur(character.data['stat_constitution'])
        character.data["armure"] = 10 + modificateur(character.data["stat_dexterity"])
    elif classe_max == 'Barde':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Clerc':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir cloute"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir cloute", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Druide':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Peaux"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Peaux", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Guerrier':
        character.data['pv_max'] = 10 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuirasse"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuirasse", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Paladin':
        character.data['pv_max'] = 10 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Chemise de Mailles"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Chemise de Mailles", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Rodeur':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Roublard':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Occultiste':
        character.data['pv_max'] = 8 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Matelassee"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Matelassee", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Magicien':
        character.data['pv_max'] = 6 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    elif classe_max == 'Ensorceleur':
        character.data['pv_max'] = 6 + modificateur(character.data['stat_constitution'])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])

    character.data['pv'] = character.data['pv_max']
    character.save(f"data/save/character/{character.data['name']}.txt")

    # Résumé
    result_text = "\n--- Résumé du personnage ---\n"
    for key, value in character.data.items():
        result_text += f"{key} : {value}\n"
    result_text += "\n--- Compétences ---\n"
    for key, value in character.data.items():
        if key.startswith('competence_') and value:
            result_text += f"{key.replace('competence_', '').capitalize()} : Oui\n"
        elif key.startswith('sauvegarde_') and value > 0:
            result_text += f"{key.replace('sauvegarde_', '').capitalize()} : {value}\n"
    result_text += f"\nAlignement : {character.data['alignment']}\n"
    result_text += f"Classe : {character.data['classe']}\n"
    result_text += f"Historique : {character.data['historique']}\n"
    result_text += f"Outils : {outils}\n"
    result_text += f"Nom : {character.data['name']}\n"
    result_text += f"Race : {character.data['race']}\n"
    result_text += f"Niveau : {character.data['level']}\n"
    result_text += "Statistiques :\n"
    for key, value in character.data.items():
        if key.startswith('stat_'):
            result_text += f"  {key.replace('stat_', '').capitalize()} : {value}\n"

    show_result("Résumé du personnage", character, outils)
    character.save(f"data/save/character/{character.data['name']}.txt")

if __name__ == '__main__':
    qcm()