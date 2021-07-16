from datetime import date
from Models.Animal import Animal
from Models.Chat import Chat
from Models.Chien import Chien
# from Models.Oiseau import Oiseau


class Animalerie:
    def __init__(self, liste_animaux) -> None:
        self.__listeAnimaux: list[Animal] = liste_animaux

    @property
    def ListeAnimaux(self) -> list:
        return self.__listeAnimaux

    @ListeAnimaux.setter
    def ListeAnimaux(self, value) -> None:
        self.__listeAnimaux = value

    def add_animal(self, item: Animal) -> None:
        if item not in self.ListeAnimaux:
            self.__listeAnimaux.append(item)

    def remove_animal(sel, item: Animal) -> None:
        pass

    TYPE_ANIMAUX: tuple = ("chat", "chien", "oiseau")

    def create_animal(self):
        animal: str = (f"Type de l'animal {Animalerie.TYPE_ANIMAUX}: ")
        while animal not in Animalerie.TYPE_ANIMAUX:
            animal = (f"Type de l'animal {Animalerie.TYPE_ANIMAUX}: ")

        nom: str = input("Nom de l'animal: ")

        poids: float = input("Poids: ")
        while poids <= 0:
            poids = input("Poids: ")

        taille: float = input("Taille: ")
        while taille <= 0:
            taille = input("Taille: ")

        sexe: str = input(
            "Sexe ('M' pour mâle, 'F' pour femelle, 'I' pour indéfini): ")
        date_naissance: date = date(
            input("Date de naissance (yyyy, mm, dd): "))
        date_arrivee: date = date(input("Date d'arrivé (yyyy, mm, dd): "))

        if animal == "chat":
            charactere: list = input("Charatères de l'animal (liste): ")
            griffe_coupee: bool = input(
                "L'animal a t'il les griffes coupées? True/False: ")
            poils: str = input("Type de poils: ")

            return Chat(nom, poids, taille, sexe, date_naissance, date_arrivee, charactere, griffe_coupee, poils)

        elif animal == "chien":
            pass
        else:
            pass

    def formulaire_chat(self) -> None:
        pass
