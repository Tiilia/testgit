from datetime import date
from Models.Animal import Animal


class Chien(Animal):
    def __init__(self, nom: str, poids: float, taille: float, sexe: str, date_naissance: date, date_arrivee: date, couleur_colier: str, est_dresseé: bool, race: str) -> None:
        super().__init__(nom, poids, taille, sexe, date_naissance, date_arrivee)
        self.__couleurCollier: str = couleur_colier  # modifiable

        if type(est_dresseé) is not bool:
            raise TypeError("Le type doit être bool")
        self.__estDressé: bool = est_dresseé         # read-only

        self.__race: str = race                      # read-only

    # Clouleur colier
    @property
    def CouleurColier(self):
        return self.__couleurCollier

    @CouleurColier.setter
    def CouleurColier(self, value):
        self.__couleurCollier = value

    # Est dressé
    @property
    def EstDressé(self):
        if self.__estDressé:
            return "Oui"
        else:
            return "Non"

    # Race
    @property
    def Race(self):
        return self.__race

    # probabilité déces
    @property
    def ProbabiliteDeces(self) -> int:
        return 1

    # Age humain
    def AgeHumain(self) -> int:
        return self.Age * 7

    # Crier
    def crier(self) -> str:
        return f"{self.Nom} aboie "

    # protocol str
    def __str__(self) -> str:
        return f"""
{super().__str__()}
Couleur du colier: {self.CouleurColier}
Est dressé: {self.EstDressé}
Race: {self.Race}
{self.crier()} """
