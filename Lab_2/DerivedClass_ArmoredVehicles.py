import BaseClass
class ArmoredVehicles(BaseClass.Weapon):
    def __init__(self, weapon_type : str = "EMPTY", company_name : str = "EMPTY", model : str = "EMPTY", caliber : float = 0.0, engine_power : int = 0):
        self.weapon_type = weapon_type
        self.company_name = company_name
        self.model = model
        self.caliber = caliber
        self.engine_power = engine_power

    def __str__(self)->str:
        return f"Тип оружия: {self.weapon_type}\nПроизводитель: {self.company_name} Модель: {self.model}\nКалибр основного орудия (в мм): {self.caliber}\nМощность двигателя (в л.с.): {self.engine_power}\n"

    def __repr__(self)->str:
        return "ArmoredVehicles: " + self.__str__()
