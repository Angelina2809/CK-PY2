class Household_appliances:
    def __init__(self, serial_number: str, power: int, weight:float):
        """
        Создание и подготовка к работе объекта "Бытовая техника"
        :param serial_number - Серийный номер
        :param power - Мощность
        :param weight - Вес
        """
        if not isinstance(power, int):
            raise TypeError("Мощность должно быть int")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательным числом")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным числом")
        self.serial_number = serial_number
        self.power = power
        self.weight = weight
    def __str__(self) -> str:
        #return "Серийный номер:\"" + self.serial_number + "\" , мощность:" + self.power
        return "Серийный номер:  " + self.serial_number + " , мощность:  " + str(self.power) + ", вес: " + str(self.weight)
    def __repr__(self):
        return "Household_appliances(serial_number="+self.serial_number+", power= "+ str(self.power)+",weight="+str(self.weight)+")"
    def inclusion(self):
        """
        Функция которая отвечает за включение прибора
        :return:
        """
        print("Machine is ON")
class Washing_machine(Household_appliances):
    def __init__(self, serial_number: str, power: int, weight:float, laundry_load:int, firm:str):
        """
        Создание и подготовка к работе объекта "Стиральная машина"
        :param serial_number - Серийный номер(наследованное свойство)
        :param power - Мощность(наследованное свойство)
        :param weight - Вес(наследованное свойство)
        :param laundry_load - Загрузка белья (кг)
        :param firm - Фирма производитель
        """
        super().__init__(serial_number, power, weight)
        if not isinstance(laundry_load, int):
            raise TypeError("Загрузка белья должно быть int")
        if laundry_load < 0:
            raise ValueError("Загрузка белья не может быть отрицательным числом")
        self.laundry_load = laundry_load
        self.firm = firm
    def __str__(self):
        return super().__str__() + " , Загрузка белья:  " + str(self.laundry_load) + " ,  Фирма производитель: " + str(self.firm)
    def __repr__(self):
        return "Household_appliances(serial_number=" + self.serial_number + ", power= " + str(self.power) + ",weight=" +str(self.weight) + ",laundry_load=" + str(self.laundry_load) +" ,firm=" + self.firm +")"
household_appliances = Household_appliances("123fg14", 2200, 30)
print(household_appliances)
print(repr(household_appliances))
washing_machine=Washing_machine("123fg14", 2200, 30,5,"samsung")
washing_machine.inclusion()
print(washing_machine)
print(repr(washing_machine))
