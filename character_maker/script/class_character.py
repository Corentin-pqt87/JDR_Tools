# -*- coding: utf-8 -*-
import os
from .class_arme import *
from .class_armure import *

class Character :
    """classe qui représente une fiche de personnage de donjon et dragon"""
    def __init__(self):
        self.data = {
            "name": "",
            "level": 1,
            "class": "",
            "race": "",
            "alignment": "",
            "historique":"",
            "stat_force": 0,
            "stat_dexterity": 0,
            "stat_constitution": 0,
            "stat_intelligence": 0,
            "stat_sagesse": 0,
            "stat_charisme": 0,
            "bonus_maitrise": 2,
            "pv_max": 10,
            "pv_actuel": 10,
            "armure": 0,
            "armure_type": None,
            "arme_principale": None,
            "arme_secondaire": None,
            "initiative": 0,
            "vitesse": 7.5,
            "sauvegarde_force": 0,
            "sauvegarde_dexterite": 0,
            "sauvegarde_constitution": 0,
            "sauvegarde_intelligence": 0,
            "sauvegarde_sagesse": 0,
            "sauvegarde_charisme": 0,
            "competence_acrobatie": False,
            "competence_arcanes": False,
            "competence_athletisme": False,
            "competence_escamotage": False,
            "competence_discretion": False,
            "competence_histoire": False,
            "competence_intimidation": False,
            "competence_investigation": False,
            "competence_medic": False,
            "competence_nature": False,
            "competence_perception": False,
            "competence_persuasion": False,
            "competence_religion": False,
            "competence_survie": False,
            "competence_tromperie": False,
            "inventaire": []
        }
    def save(self, filename):
        """sauvegarde la fiche de personnage dans un fichier"""
        with open(filename, 'w') as file:
            for key, value in self.data.items():
                file.write(f"{key}: {value}\n")

    def load(self, filename):
        """charge la fiche de personnage depuis un fichier"""
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or ": " not in line:
                    continue  # Ignore les lignes vides ou incorrectes
                parts = line.split(": ", 1)
                if len(parts) != 2:
                    continue  # Ignore si la ligne n'a pas exactement une clé et une valeur
                key, value = parts
                # Conversion automatique des types
                if value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit() and '.' in value:
                    value = float(value)
                elif value == "True":
                    value = True
                elif value == "False":
                    value = False
                self.data[key] = value
    def __str__(self):
        """affiche la fiche de personnage sous forme de chaîne de caractères"""
        return "\n".join(f"{key}: {value}" for key, value in self.data.items())

def modificateur(stat):
    """calcule le modificateur d'une statistique"""
    return (int(stat) - 10) // 2


if __name__ == "__main__":
    # Efacer le fichier test_character.txt avant de le remplir
    with open('test_character.txt', 'w') as file:   
        file.write("")
    # Exemple d'utilisation de la classe Character
    character = Character()
    character.data['name'] = 'Héros'
    character.data['class'] = 'Guerrier'
    armure_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'base', 'item', 'armure.txt')
    armure_path = os.path.normpath(armure_path)
    character.data['armor_type'] = armure_get_by_name("Cuir", armure_path)
    character.data['stat_force'] = 16
    character.data['stat_dexterity'] = 14
    character.data['stat_constitution'] = 15
    character.data['stat_intelligence'] = 10
    character.data['stat_sagesse'] = 12
    character.data['stat_charisme'] = 8

    character.save('test_character.txt')
    print("================================================")
    new_character = Character()
    new_character.load('test_character.txt')
    print(new_character)
    

    