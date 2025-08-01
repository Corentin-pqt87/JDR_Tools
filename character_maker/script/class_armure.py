from random import random
from hashlib import sha256
class Armure:
    def __init__(self,name='None'):
        # Unique ID based on the name
        self.id = sha256(name.encode()).hexdigest()
        self.data = {
            "name": name,
            "type": "",
            "armor_class": 0,
            "weight": 0,
            "properties": []
        }
    def __str__(self):
        """affiche les détails de l'armure sous forme de chaîne de caractères"""
        return "\n".join(f"{key}: {value}" for key, value in self.data.items())
    
    def save(self, filename):
        """sauvegarde les détails de l'arme dans un fichier"""
        #plusieurs objets peuvent être sauvegardés dans le même fichier
        #la première ligne contient l'ID, les autres lignes contiennent les détails de l'arme
        #si a la suite on trouve un autre ID, c'est que c'est une autre arme, on l'écrit a la suite séparer par une ligne vide
        with open(filename, 'a') as file:   
            file.write(f"ID: {self.id}\n")
            for key, value in self.data.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
def load_armure(filename):
        """charge les détails de plusieurs armures depuis un fichier"""
        armures = []
        with open(filename, 'r') as file:
            current_armure = None
            for line in file:
                line = line.strip()
                if not line:
                    if current_armure:
                        armures.append(current_armure)
                        current_armure = None
                    continue
                if line.startswith("ID: "):
                    if current_armure:
                        armures.append(current_armure)
                    current_armure = Armure("")
                    current_armure.id = str(line.split(": ")[1])
                elif ": " in line and current_armure is not None:
                    key, value = line.split(": ", 1)
                    current_armure.data[key] = value
            if current_armure:
                armures.append(current_armure)
        return armures  

def armure_get_by_id(id, filename):
    """Récupère une armure par son ID depuis un fichier"""
    armures = load_armure(filename)
    for armure in armures:
        if armure.id == id:
            return armure
def armure_get_by_name(name, filename):
    """Récupère une armure par son nom depuis un fichier"""
    armures = load_armure(filename)
    for armure in armures:
        if armure.data['name'] == name:
            return armure
    return None  # Si aucune armure avec ce nom n'est trouvée   

def armure_get_by_type(type, filename):
    """Récupère une liste des armures du meme type depuis un fichier et retourne une liste de noms d'armures"""
    armures = load_armure(filename)
    armures_type = []
    for armure in armures:
        if armure.data['type'] == type:
            armures_type.append(armure.data['name'])
    return armures_type

def create_armure_file():
    """Crée un fichier d'armures de base pour DnD 5e"""
    #Efacer le fichier test_armure.txt avant de le remplir
    with open('test_armure.txt', 'w') as file:
        file.write("")
    # Ajout des armures de DnD 5e
    Matelassee = Armure("Matelassee")
    Matelassee.data['type'] = "Légère"
    Matelassee.data['armor_class'] = 11
    Matelassee.data['weight'] = 10
    Matelassee.data['properties'] = ["Desavantage en Discrétion"]
    Matelassee.save('data/base/item/armure.txt')

    cuir = Armure("Cuir")
    cuir.data['type'] = "Légère"
    cuir.data['armor_class'] = 11
    cuir.data['weight'] = 10
    cuir.save('data/base/item/armure.txt')

    cuir_cloute = Armure("Cuir Cloute")
    cuir_cloute.data['type'] = "Légère"
    cuir_cloute.data['armor_class'] = 12
    cuir_cloute.data['weight'] = 13
    cuir_cloute.save('data/base/item/armure.txt')

    Peaux = Armure("Peaux")
    Peaux.data['type'] = "Légère"
    Peaux.data['armor_class'] = 12
    Peaux.data['weight'] = 10
    Peaux.save('data/base/item/armure.txt')

    Chemise_mailles = Armure("Chemise de Mailles")
    Chemise_mailles.data['type'] = "Légère"
    Chemise_mailles.data['armor_class'] = 13   
    Chemise_mailles.data['weight'] = 20
    Chemise_mailles.save('data/base/item/armure.txt')

    ecailles = Armure("Ecailles")
    ecailles.data['type'] = "Moyenne"
    ecailles.data['armor_class'] = 13
    ecailles.data['weight'] = 20
    ecailles.data['properties'] = ["Desavantage en Discrétion"]
    ecailles.save('data/base/item/armure.txt')

    cuirasse = Armure("Cuirasse")
    cuirasse.data['type'] = "Moyenne"
    cuirasse.data['armor_class'] = 14
    cuirasse.data['weight'] = 30
    cuirasse.save('data/base/item/armure.txt')

    demi_plate = Armure("Demi-Plate")
    demi_plate.data['type'] = "Moyenne"
    demi_plate.data['armor_class'] = 15
    demi_plate.data['weight'] = 40
    demi_plate.data['properties'] = ["Desavantage en Discrétion"]
    demi_plate.save('data/base/item/armure.txt')

    broigne = Armure("Broigne")
    broigne.data['type'] = "Lourde"
    broigne.data['armor_class'] = 14
    broigne.data['weight'] = 40
    broigne.data['properties'] = ["Desavantage en Discrétion"]
    broigne.save('data/base/item/armure.txt')

    cotte_mailles = Armure("Cotte de Mailles")
    cotte_mailles.data['type'] = "Lourde"
    cotte_mailles.data['armor_class'] = 16
    cotte_mailles.data['weight'] = 55
    cotte_mailles.data['properties'] = ["Desavantage en Discrétion"]
    cotte_mailles.save('data/base/item/armure.txt')

    clibanion = Armure("Clibanion")
    clibanion.data['type'] = "Lourde"
    clibanion.data['armor_class'] = 17
    clibanion.data['weight'] = 60
    clibanion.data['properties'] = ["Desavantage en Discrétion"]
    clibanion.save('data/base/item/armure.txt')

    harnois = Armure("Harnois")
    harnois.data['type'] = "Lourde"
    harnois.data['armor_class'] = 18
    harnois.data['weight'] = 65
    harnois.data['properties'] = ["Desavantage en Discrétion"]
    harnois.save('data/base/item/armure.txt')


if __name__ == "__main__":
    print(
        armure_get_by_name('Peaux', "data/base/item/armure.txt").data['armor_class']
    )
    print(
        type(armure_get_by_name('Peaux', "data/base/item/armure.txt").data['armor_class'])
    )