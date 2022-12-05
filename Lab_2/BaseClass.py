class Weapon:
    def __init__(self, weapon_type : str = "EMPTY", company_name : str = "EMPTY", model : str = "EMPTY"):
        self.weapon_type = weapon_type
        self.company_name = company_name
        self.model = model

    def __str__(self)->str:
        return f"Тип оружия: {self.weapon_type}\nПроизводитель: {self.company_name} Модель: {self.model}"

    def __repr__(self)->str:
        return "Weapon: " + self.__str__()
