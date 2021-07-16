from datetime import date
from Models.Animal import Animal


class Chat(Animal):
    def __init__(self, nom: str, poids: float, taille: float, sexe: str, date_naissance: date, date_arrivee: date, charactere: list, griffe_coupee: bool, poils: str) -> None:
        """ 
        charactère : liste ["énergique", "farouche", "câlin", ...]
        griffe coupée: True ou False
        poils : "court", "long", ...
         """
        super().__init__(nom, poids, taille, sexe, date_naissance, date_arrivee)
        self.__charactere: list = charactere               # modifiable
        self.__griffeCoupee: bool = griffe_coupee          # modifiable
        self.__poils: str = poils                          # read-only

    # Charactere ---------------------------------------------
    @property
    def Charactere(self) -> str:
        return self.__charactere

    @Charactere.setter
    def Charactere(self, value):
        self.__charactere = value

    # GriffeCoupe --------------------------------------------------
    @property
    def GriffeCoupee(self) -> str:
        if self.__griffeCoupee:
            return "Oui"
        else:
            return "Non"

    @GriffeCoupee.setter
    def GriffeCoupee(self, value: bool) -> None:
        self.__griffeCoupee = value

    # Poils ---------------------------------------------------------
    @property
    def Poils(self) -> str:
        return self.__poils

     # AgeHumain ---------------------------------------------
    def AgeHumain(self) -> int:
        if self.Age >= 2:
            return (self.Age - 2) * 4 + 24
        elif self.AgeMonth > 18:
            return 21
        elif self.AgeMonth > 12:
            return 15
        elif self.AgeMonth > 8:
            return 12
        elif self.AgeMonth > 6:
            return 10
        elif self.AgeMonth > 4:
            return "entre 6 et 8"
        elif self.AgeMonth >= 2:
            return "entre 2 et 4"
        else:
            return "entre 0 et 1"

    # ProbabiliteDeces ---------------------------------------------
    @property
    def ProbabiliteDeces(self) -> float:
        return 0.5

    # Crier --------------------------------------------------------
    def crier(self) -> str:
        return f"{self.Nom} est entrain de miauler"

    # le protocol str --------------------------------------------------------
    def __str__(self) -> str:
        return f""" 
{Animal.__str__(self)}
Poils {self.Poils}
Charactère: {", ".join(self.Charactere)}
Griffes coupées: {self.GriffeCoupee} 
{self.crier()}
"""
