class Car:
    # Атрибуты класса
    make = ""
    model = ""
    year = 0
    color = ""

    # Конструктор класса (специальный метод __init__)
    def __init__(self, make='mazda', model='6', year='2011', color='gray'):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Метод для вывода информации о машине
    def display_info(self):
        print(f"Марка: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")

    # Метод для запуска двигателя
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигатель запущен")

    # Метод для остановки двигателя
    def stop_engine(self):
        print(f"{self.make} {self.model}: Двигатель остановлен")

    def __str__(self):
        return f'{self.make.capitalize()} {self.model.capitalize()}'
