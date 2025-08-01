from random import random
from hashlib import sha256

class Arme:
    def __init__(self,name='None'):
        # Unique ID based on the name
        self.id = sha256(name.encode()).hexdigest()
        self.data = {
            "name": name,
            "type": "",
            "damage": "",
            "damage_type": "",
            "weight": 0,
            "properties": []
        }
    def __str__(self):
        """affiche les détails de l'arme sous forme de chaîne de caractères"""
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

        
def load_arme(filename):
    """charge les détails de plusieurs armes depuis un fichier"""
    # Si il y a plusieurs armes dans le fichier, on les charge toutes
    # Une ligne vide sépare les armes
    armes = []
    with open(filename, 'r') as file:
        current_arme = None
        for line in file:
            line = line.strip()
            if not line:
                if current_arme:
                    armes.append(current_arme)
                    current_arme = None
                continue
            if line.startswith("ID: "):
                if current_arme:
                    armes.append(current_arme)
                current_arme = Arme("")
                current_arme.id = str(line.split(": ")[1])
            elif ": " in line and current_arme is not None:
                key, value = line.split(": ", 1)
                current_arme.data[key] = value
        if current_arme:
            armes.append(current_arme)
    return armes

def arme_get_by_id(id, filename):
    """Récupère une arme par son ID depuis un fichier"""
    armes = load_arme(filename)
    for arme in armes:
        if arme.id == id:
            return arme
def arme_get_by_name(name, filename):
    """Récupère une arme par son nom depuis un fichier"""
    armes = load_arme(filename)
    for arme in armes:
        if arme.data['name'] == name:
            return arme
        
if __name__ == "__main__":
    #Efacer le fichier test_arme.txt avant de le remplir
    with open('test_arme.txt', 'w') as file:
        file.write("")
    # Exemple d'utilisation de la classe Arme
    arme_1 = Arme("épée Longue")
    arme_1.data['type'] = 'Mêlée'
    arme_1.data['damage'] = '1d8'
    arme_1.data['damage_type'] = 'Tranchant'
    arme_1.data['weight'] = 3
    print(arme_1)
    print(f"ID de l'arme: {arme_1.id}")
    arme_1.save('test_arme.txt')

    arme_2 = Arme("Arc Long")
    arme_2.data['type'] = 'Distance'
    arme_2.data['damage'] = '1d8'
    arme_2.data['damage_type'] = 'Perforant'
    arme_2.data['weight'] = 2
    print(arme_2)
    print(f"ID de l'arme: {arme_2.id}")
    arme_2.save('test_arme.txt')
    print("================================================")

    lst_arme = load_arme('test_arme.txt')
    ouput_arme_1 = lst_arme[0]
    ouput_arme_2 = lst_arme[1]
    print(ouput_arme_1)
    print(ouput_arme_1.id)
    print(ouput_arme_2)
    print(ouput_arme_2.id)