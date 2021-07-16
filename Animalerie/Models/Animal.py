from abc import ABC, abstractmethod
from datetime import date


class Animal(ABC):
    def __init__(self, nom: str, poids: float, taille: float, sexe: str, date_naissance: date, date_arrivee: date) -> None:
        """ 
        date_naissance et date_arrivee en date(yyyy,mm,dd) 
        poid en kg
        taille en cm
        sexe: M = mâle, F = femelle, ou I = indéfini
        """
        # ------- Validation  sexe----------------
        # if sexe != "H" and sexe != "F" and sexe != "I"  --> écriture classique dans tous les langages
        # if sexe not in "HFI" ----------- écriture simplifiée python ---- tuple, list ou str
        if sexe not in Animal.SEXES_VALUES:  #
            raise ValueError("Sexe invalide")
        self.__sexe: str = sexe                     # read-only

        self.__nom: str = nom                       # read-only

        if poids <= 0:
            raise ValueError("Poids invalide")
        self.__poids: float = poids                 # modifiable

        if taille <= 0:
            raise ValueError("Taille invalide")
        self.__taille: float = taille               # modifiable

        if date.today() < date_naissance:
            raise ValueError(
                "L'animal ne peut être né à une date ultérieur à aujourd'hui")
        self.__dateNaiss: date = date_naissance    # read-only

        if date_arrivee < date_naissance:
            raise ("L'animal ne peut pas entrer avant sa naissance")
        self.__dateArrivee: date = date_arrivee    # read-only

        Animal.compteur_animal += 1

    # Nom -------------------------------------------------------------------------------------------------
    @property
    def Nom(self) -> str:
        return self.__nom

    # Taille ------------------------------------------------------------------------------------------------
    @property
    def Taille(self) -> str:
        return self.__taille

    @Taille.setter
    def Taille(self, value):
        self.__taille = value

    # Poids -------------------------------------------------------------------------------------------------
    @property
    def Poids(self) -> str:
        return self.__poids

    @Poids.setter
    def Poids(self, value):
        self.__poids = value

    # Sexe ----------------------------------------------------------------------------------------------------
    @property
    def Sexe(self) -> str:
        if self.__sexe == "M":
            return "Mâle"
        elif self.__sexe == "F":
            return "Femelle"
        else:
            return "Indéfini"

    # DateNaiss -------------------------------------------------------------------------------------------------
    @property
    def DateNaiss(self) -> str:
        return self.__dateNaiss

    # DateArrivee ------------------------------------------------------------------------------------------------
    @property
    def DateArrivee(self) -> str:
        return self.__dateArrivee

    # Age --------------------------------------------------------------------------------------------------------
    @property
    def Age(self) -> int:
        return int((date.today() - self.DateNaiss).days / 365.2425)

    @property
    def AgeMonth(self) -> int:
        return int((date.today() - self.DateNaiss).days / 365.2425 * 12)

    # Crier ------------------------------------------------------------------------------------------------------
    def crier(self) -> str:
        return f"{self.Nom} est entrain de crier"

    # AgeHumain ---------------------------------------------------------------------------------------------------
    @abstractmethod
    def AgeHumain(self) -> int:
        pass

    # ProbabiliteDeces ---------------------------------------------------------------------------------------------
    @property  # attention à l'ordre
    @abstractmethod
    def ProbabiliteDeces(self):
        pass

    # Le protocole str/ Le data model str  ----------------------------------------------------------------------------
    def __str__(self) -> str:
        age_str = f"{self.Age} ans" if self.Age > 2 else f"{self.AgeMonth} mois"
        # sexe_str = "Mâle" if self.Sexe == "M" "Femelle" elif self.Age == "F" else "Indéfini"
        return f"""
    Animal: {type(self).__name__}
Nom: {self.Nom}
Sexe: {self.Sexe}
Age: {age_str}, {self.AgeHumain()} ans en âge humain
Poids: {self.Poids}kg
Taille: {self.Taille}cm
Arrivé(e) le {self.DateArrivee.day} du {self.DateArrivee.month} en {self.DateArrivee.year}
Probalité de déces: {self.ProbabiliteDeces}% """

    # méthode statique
    # @staticmethod
    # def get_available_gender():
    #     return SEXES_VALUES

    SEXES_VALUES = ("M", "F", "I")
    compteur_animal = 0
    id_animal = compteur_animal + 1
