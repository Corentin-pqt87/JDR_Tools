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
    answer = simpledialog.askstring(
        title,
        question + "\n" + "\n".join([f"{i+1}. {c}" for i, c in enumerate(choices)])
    )
    root.destroy()
    return answer

def show_result(title, character):
    root = tk.Tk()
    root.title(title)
    root.geometry("900x500")
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    infos = [
        ("Nom", character.data.get("name", "")),
        ("Race", character.data.get("race", "")),
        ("Classe", character.data.get("class", "")),
        ("Niveau", character.data.get("niveau", "")),
        ("Alignement", character.data.get("alignment", "")),
        ("Historique", character.data.get("historique", "")),
        ("Outils", character.data.get("outils", "")),
        ("PV", character.data.get("pv", "")),
        ("PV max", character.data.get("pv_max", "")),
        ("Armure", character.data.get("armure", "")),
        ("Type armure", character.data.get("armure_type", "")),
    ]
    stats = [(k.replace("stat_", "").capitalize(), v) for k, v in character.data.items() if k.startswith("stat_")]
    competences = [(k.replace("competence_", "").capitalize(), "Oui") for k, v in character.data.items() if k.startswith("competence_") and v]
    sauvegardes = [(k.replace("sauvegarde_", "").capitalize(), v) for k, v in character.data.items() if k.startswith("sauvegarde_") and v > 0]

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

    tk.Button(root, text="Fermer", command=root.destroy).pack(pady=10)
    root.mainloop()

def etape_par_etape_RUN():
    character = Character()

    character.data["name"] = ask_string("Nom", "Entrez le nom de votre personnage :")
    character.data["alignment"] = ask_string("Alignement", "Entrez l'alignement de votre personnage :")
    race_lst = [
        "Humain", "Elfe", "Nain", "Halfelin", "Dragonborn",
        "Tiefling", "Gnome", "Demi-orc", "Demi-elfe"
    ]
    race = ""
    while race not in race_lst:
        race = ask_string("Race", "Entrez la race de votre personnage :\n" + ", ".join(race_lst))
    character.data["race"] = race

    # Race bonus
    if race == "Humain":
        for stat in [
            "stat_force", "stat_dexterity", "stat_constitution",
            "stat_intelligence", "stat_sagesse", "stat_charisme"
        ]:
            character.data[stat] = 1
        character.data["vitesse"] = 9
    elif race == "Elfe":
        character.data["stat_dexterity"] = 2
        character.data["vitesse"] = 9
        sous_race = ask_string("Sous-race", "Entrez la sous-race de votre elfe :\nElfe des bois, Elfe des neiges, Elfe noir, Haut-elfe")
        if sous_race == "Elfe des bois":
            character.data["stat_sagesse"] = 1
        elif sous_race == "Elfe des neiges":
            character.data["stat_constitution"] = 1
        elif sous_race == "Elfe noir":
            character.data["stat_charisme"] = 1
        elif sous_race == "Haut-elfe":
            character.data["stat_intelligence"] = 1
    elif race == "Nain":
        character.data["stat_constitution"] = 2
        character.data["vitesse"] = 7.5
        sous_race = ask_string("Sous-race", "Entrez la sous-race de votre nain :\nNain des montagnes, Nain des collines, Nain des profondeurs")
        if sous_race == "Nain des montagnes":
            character.data["stat_force"] = 1
        elif sous_race == "Nain des collines":
            character.data["stat_sagesse"] = 1
        elif sous_race == "Nain des profondeurs":
            character.data["stat_charisme"] = 1
    elif race == "Halfelin":
        character.data["stat_dexterity"] = 2
        character.data["vitesse"] = 7.5
        sous_race = ask_string("Sous-race", "Entrez la sous-race de votre halfelin :\nHalfelin des champs, Halfelin des collines, Halfelin des profondeurs")
        if sous_race == "Halfelin des champs":
            character.data["stat_force"] = 1
        elif sous_race == "Halfelin des collines":
            character.data["stat_sagesse"] = 1
        elif sous_race == "Halfelin des profondeurs":
            character.data["stat_charisme"] = 1
    elif race == "Dragonborn":
        character.data["stat_force"] = 2
        character.data["vitesse"] = 9
        couleur = ask_string("Couleur", "Entrez la couleur de votre dragonborn :\nRouge, Bleu, Vert, Noir, Blanc")
        if couleur in ["Rouge", "Bleu", "Vert", "Noir", "Blanc"]:
            character.data["stat_charisme"] = 1
    elif race == "Tiefling":
        character.data["stat_charisme"] = 2
        character.data["vitesse"] = 9
        sous_race = ask_string("Sous-race", "Entrez la sous-race de votre tiefling :\nTiefling des enfers, Tiefling des abysses, Tiefling des ombres")
        if sous_race == "Tiefling des enfers":
            character.data["stat_force"] = 1
        elif sous_race == "Tiefling des abysses":
            character.data["stat_dexterity"] = 1
        elif sous_race == "Tiefling des ombres":
            character.data["stat_intelligence"] = 1
    elif race == "Gnome":
        character.data["stat_intelligence"] = 2
        character.data["vitesse"] = 7.5
        sous_race = ask_string("Sous-race", "Entrez la sous-race de votre gnome :\nGnome des forêts, Gnome des montagnes, Gnome des profondeurs")
        if sous_race == "Gnome des forêts":
            character.data["stat_dexterity"] = 1
        elif sous_race == "Gnome des montagnes":
            character.data["stat_constitution"] = 1
        elif sous_race == "Gnome des profondeurs":
            character.data["stat_charisme"] = 1
    elif race == "Demi-orc":
        character.data["stat_force"] = 2
        character.data["vitesse"] = 9
    elif race == "Demi-elfe":
        character.data["stat_charisme"] = 2
        character.data["vitesse"] = 9
        for stat in ["stat_force", "stat_dexterity", "stat_constitution", "stat_intelligence", "stat_sagesse"]:
            choice = ask_string("Bonus demi-elfe", f"Voulez-vous augmenter {stat} de +1 ? (oui/non)")
            if choice and choice.lower() == "oui":
                character.data[stat] += 1

    # Caractéristiques
    valeur_distribuees = [15, 14, 13, 12, 10, 8]
    for stat in ["stat_force", "stat_dexterity", "stat_constitution", "stat_intelligence", "stat_sagesse", "stat_charisme"]:
        val = None
        while val not in valeur_distribuees:
            val = ask_int("Caractéristique", f"Entrez la valeur pour {stat.replace('stat_', '').capitalize()} :\n{valeur_distribuees}", minval=min(valeur_distribuees), maxval=max(valeur_distribuees))
        valeur_distribuees.remove(val)
        character.data[stat] = val

    # Classe
    classe_lst = [
        "Barbare", "Barde", "Clerc", "Druide", "Guerrier", "Moine", "Paladin", "Rôdeur", "Roublard",
        "Ensorceleur", "Magicien", "Ocultiste"
    ]
    classe = ""
    while classe not in classe_lst:
        classe = ask_string("Classe", "Entrez la classe de votre personnage :\n" + ", ".join(classe_lst))
    character.data["class"] = classe

    # Niveau
    niveau = ask_int("Niveau", "Entrez le niveau de votre personnage :", 1, 20)
    character.data["niveau"] = niveau

    # Armure et PV selon la classe (exemple pour Barbare, à compléter pour les autres classes)
    if classe == "Barbare":
        character.data["stat_force"] += 2
        character.data["stat_constitution"] += 1
        character.data["armure"] = 10 + modificateur(character.data["stat_dexterity"])
        character.data["pv_max"] = 12 + modificateur(character.data["stat_constitution"])
    elif classe == "Barde":
        character.data["stat_charisme"] += 2
        character.data["stat_dexterity"] += 1
        character.data["pv_max"] = 8 + modificateur(character.data["stat_constitution"])
        character.data['armure_type'] = "Cuir"
        character.data["armure"] = modificateur(character.data["stat_dexterity"]) + int(armure_get_by_name("Cuir", "data/base/item/armure.txt").data['armor_class'])
    # ... (complète pour chaque classe comme dans ton code d'origine)

    character.data["pv"] = character.data["pv_max"]

    # Compétences (exemple, à adapter selon la classe)
    # Pour chaque classe, tu peux demander les compétences avec ask_choice ou ask_string

    # Outils (exemple)
    character.data["outils"] = ask_string("Outils", "Entrez les outils de votre personnage (séparés par des virgules) :")

    # Historique
    character.data["historique"] = ask_string("Historique", "Entrez l'historique de votre personnage :")

    # Résumé
    show_result("Résumé du personnage", character)

    character.save(f"data/save/character/{character.data['name']}.txt")
    return True

if __name__ == "__main__":
    etape_par_etape_RUN()