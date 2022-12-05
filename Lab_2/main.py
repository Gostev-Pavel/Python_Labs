from BaseClass import *
from DerivedClass_Handguns import *
from DerivedClass_ArmoredVehicles import *
from CollectionClass_MilitaryCompany import *

military_company = MilitaryCompany("Academi",
                [
                    Handguns("Штурмовая винтовка", "Colt", "Model 920", 5.56, 1994),
                    Handguns("Автоматический пистолет", "Glock", "18", 9.0, 1989)
                ],
                [
                    ArmoredVehicles("БМП", "США", "M2 Bradley", 25.0, 500),
                    ArmoredVehicles("Военный внедорожник", "США", "HMMWV", 12.7, 195)
                ])
SerialiseMilitaryCompany(military_company, "lab2.json")
print("После сериализации:\n")
print(military_company)
deserialised_company = DeserialiseMilitaryCompany("lab2.json")
print("После десериализации:\n")
print(deserialised_company)
