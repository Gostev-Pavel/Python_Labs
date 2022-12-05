import BaseClass
class Handguns(BaseClass.Weapon):
    def __init__(self, weapon_type : str = "EMPTY", company_name : str = "EMPTY", model : str = "EMPTY", caliber : float = 0.0, production_year : int = 0):
        self.weapon_type = weapon_type
        self.company_name = company_name
        self.model = model
        self.caliber = caliber
        self.production_year = production_year

    def __str__(self)->str:
        return f"Тип оружия: {self.weapon_type}\nПроизводитель: {self.company_name} Модель: {self.model}\nКалибр (в мм): {self.caliber}\nНачало производства: {self.production_year}\n"

    def __repr__(self)->str:
        return "Handguns: " + self.__str__()
