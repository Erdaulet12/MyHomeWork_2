"""task_3.py"""


class Stadium:
    """Класс стадиона"""

    def __init__(self, name, opening_date, country, city, capacity):
        """Конструктор класса"""
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    @staticmethod
    def input_data():
        """Метод для ввода данных о стадионе"""
        name = input("Введите название стадиона: ")
        opening_date = input("Введите дату открытия стадиона: ")
        country = input("Введите страну, в которой расположен стадион: ")
        city = input("Введите город, в котором расположен стадион: ")
        capacity = int(input("Введите вместимость стадиона: "))
        return Stadium(name, opening_date, country, city, capacity)

    def output_data(self):
        """Метод для вывода данных о стадионе"""
        print("----------------------------------")
        print("Название стадиона:", self.name)
        print("Дата открытия стадиона:", self.opening_date)
        print("Страна, в которой расположен стадион:", self.country)
        print("Город, в котором расположен стадион:", self.city)
        print("Вместимость стадиона:", self.capacity)

    def get_name(self):
        """Метод для получения названия стадиона"""
        return self.name

    def get_opening_date(self):
        """Метод для получения даты открытия стадиона"""
        return self.opening_date

    def get_country(self):
        """Метод для получения страны, в которой расположен стадион"""
        return self.country

    def get_city(self):
        """Метод для получения города, в котором расположен стадион"""
        return self.city

    def get_capacity(self):
        """Метод для получения вместимости стадиона"""
        return self.capacity


if __name__ == "__main__":
    stadium = Stadium.input_data()
    stadium.output_data()
