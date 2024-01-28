# HW11_3

import logging

logging.basicConfig(level=logging.INFO)

class Rectangle:
    """
    Класс, представляющий прямоугольник.
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
        logging.info(f"Создан прямоугольник: {self}")

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        result = Rectangle(width, height)
        logging.info(f"Выполнено сложение прямоугольников: {self} + {other} = {result}")
        return result

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        result = Rectangle(width, height)
        logging.info(f"Выполнено вычитание прямоугольников: {self} - {other} = {result}")
        return result

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
        """
        return f"Rectangle({self.width}, {self.height})"
