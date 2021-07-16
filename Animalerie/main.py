from datetime import date
from Models.Animal import Animal
from Models.Chat import Chat
from Models.Animalerie import Animalerie
from Models.Chien import Chien
# from Models.Oiseau import Oiseau

chat1: Chat = Chat("Tigrou", 4.2, 40, "M", date(
    2021, 4, 10), date(2021, 6, 10), ["câlin", "timide", "gourmand"], False, "courts")
# print(chat1)
# print(chat1.ProbabiliteDeces)

chien1: Chien = Chien("Bethoveen", 15, 80, "M", date(
    2020, 1, 10), date.today(), "Rouge", True, "Dalmacien")
print(chien1)


