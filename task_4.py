"""task_4.py"""


class MainClass:
    """Главный класс"""

    def __init__(self, text_field):
        """Конструктор класса"""
        self.text_field = text_field

    def set_text_field(self, new_text=None):
        """Метод для присваивания значения текстовому полю"""
        if new_text is not None:
            self.text_field = new_text
        else:
            self.text_field = input("Введите новый текст: ")


class ChildClass(MainClass):
    """Класс-потомок"""

    def __init__(self, text_field, numeric_field):
        """Конструктор класса-потомка"""
        super().__init__(text_field)
        self.numeric_field = numeric_field


if __name__ == "__main__":

    child_instance = ChildClass(text_field="Иван", numeric_field=18)

    print("Текстовое поле:", child_instance.text_field)
    print("Числовое поле:", child_instance.numeric_field)
