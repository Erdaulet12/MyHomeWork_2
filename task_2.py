"""task_2.py"""


class Book:
    """Класс книги"""

    def __init__(self, title, year, publisher, genre, author, price):
        """Конструктор класса"""
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    @staticmethod
    def input_data():
        """Метод для ввода данных о книге"""
        title = input("Введите название книги: ")
        year = int(input("Введите год выпуска: "))
        publisher = input("Введите издателя: ")
        genre = input("Введите жанр: ")
        author = input("Введите автора: ")
        price = int(input("Введите цену: "))
        return Book(title, year, publisher, genre, author, price)

    def output_data(self):
        """Метод для вывода данных о книге"""
        print("----------------------------")
        print("Название книги:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_title(self):
        """Метод для получения названия книги"""
        return self.title

    def get_year(self):
        """Метод для получения года выпуска книги"""
        return self.year

    def get_publisher(self):
        """Метод для получения издателя книги"""
        return self.publisher

    def get_genre(self):
        """Метод для получения жанра книги"""
        return self.genre

    def get_author(self):
        """Метод для получения автора книги"""
        return self.author

    def get_price(self):
        """Метод для получения цены книги"""
        return self.price


if __name__ == "__main__":
    book = Book.input_data()
    book.output_data()
