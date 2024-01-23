class Car:
    """Класс автомобиля"""

    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        """Конструктор класса"""
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    @staticmethod
    def input_data():
        """Метод для ввода данных о автомобиле"""
        model = input("Введите название модели: ")
        year = int(input("Введите год выпуска: "))
        manufacturer = input("Введите производителя: ")
        engine_volume = float(input("Введите объем двигателя: "))
        color = input("Введите цвет машины: ")
        price = int(input("Введите цену: "))
        return Car(model, year, manufacturer, engine_volume, color, price)

    def output_data(self):
        """Метод для вывода данных о автомобиле"""
        print("---------------------------")
        print("Модель:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.manufacturer)
        print("Объем двигателя:", self.engine_volume)
        print("Цвет:", self.color)
        print("Цена:", self.price)

    def get_model(self):
        """Метод для получения названия модели автомобиля"""
        return self.model

    def get_year(self):
        """Метод для получения года выпуска автомобиля"""
        return self.year

    def get_manufacturer(self):
        """Метод для получения производителя автомобиля"""
        return self.manufacturer

    def get_engine_volume(self):
        """Метод для получения объема двигателя автомобиля"""
        return self.engine_volume

    def get_color(self):
        """Метод для получения цвета автомобиля"""
        return self.color

    def get_price(self):
        """Метод для получения цены автомобиля"""
        return self.price


if __name__ == "__main__":
    car = Car.input_data()
    car.output_data()
