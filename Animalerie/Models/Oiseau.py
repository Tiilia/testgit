from _typeshed import Self
from datetime import date
from Models.Animal import Animal


class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: float, sexe: str, date_naissance: date, date_arrivee: date, couleur: str, voilere: bool, cage: bool) -> None:
        super().__init__(nom, poids, taille, sexe, date_naissance, date_arrivee)
        self.__couleur: str = couleur  # read-only

        if cage and voilere:
            raise ValueError("Ne peut être vrai sur les deux")
        elif not cage and not voilere:
            raise ValueError("Doit être un des deux")
        self.__cage: bool = cage  # read-only
        self.__voliere: bool = cage  # read-only

    # couleur ----------------------
    @property
    def Couleur(self):
        return self.__couleur

    # cage --------------------------
    @property
    def Cage(self):
        return self.__cage

    # voliere -----------------------
    @property
    def Voliere(self):
        return self.__voliere
