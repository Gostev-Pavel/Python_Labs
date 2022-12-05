import BaseClass
import DerivedClass_Handguns
import DerivedClass_ArmoredVehicles
import json
import copy

class MilitaryCompany:
    def __init__(self, name : str = "EMPTY", handguns : list = [], armored_vehicles : list = []):
        self.name = name
        self.handguns = handguns
        self.armored_vehicles = armored_vehicles

    def __str__(self)->str:
        result = f"Военная компания: {self.name}\nИспользуемое ручное оружие:\n"
        for handgun in self.handguns:
            result += handgun.__str__() + "\n"
        result += "Используемая бронетехника:\n"
        for vehicle in self.armored_vehicles:
            result += vehicle.__str__() + "\n"
        return result

    def __repr__(self)->str:
        return self.__str__()

#Сериализация состояния в .json
def SerialiseMilitaryCompany(military_company : MilitaryCompany, path : str):
    with open(path, 'w') as output_file:
        dictionary = copy.deepcopy(military_company.__dict__)
        dictionary["handguns"] = [i.__dict__ for i in military_company.handguns]
        dictionary["armored_vehicles"] = [i.__dict__ for i in military_company.armored_vehicles]
        json.dump(dictionary, output_file, indent = 3, ensure_ascii = False)

#Десериализация состояния из .json
def DeserialiseMilitaryCompany(path: str)->MilitaryCompany:
    def Deserialise(dictionary):
        for i in MilitaryCompany().__dict__.keys():
            if not i in dictionary:
                break;
        else:
            return MilitaryCompany(dictionary["name"], [Deserialise(i) for i in dictionary["handguns"]], [Deserialise(i) for i in dictionary["armored_vehicles"]])
        for i in DerivedClass_Handguns.Handguns().__dict__.keys():
            if not i in dictionary:
                break;
        else:
            return DerivedClass_Handguns.Handguns(dictionary["weapon_type"], dictionary["company_name"], dictionary["model"], dictionary["caliber"], dictionary["production_year"])
        for i in DerivedClass_ArmoredVehicles.ArmoredVehicles().__dict__.keys():
            if not i in dictionary:
                break;
        else:
            return DerivedClass_ArmoredVehicles.ArmoredVehicles(dictionary["weapon_type"], dictionary["company_name"], dictionary["model"], dictionary["caliber"], dictionary["engine_power"])
    with open(path, 'r') as input_file:
        data = json.load(input_file)
        return Deserialise(data)
