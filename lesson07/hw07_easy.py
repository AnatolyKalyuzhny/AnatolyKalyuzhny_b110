# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math
class Triangle:
    """
    точки в формате A(0, 1), B(5, 2), C(9, 1)
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.ab = self._calculate_side(a, b)
        self.bc = self._calculate_side(b, c)
        self.ca = self._calculate_side(c, a)

    def _calculate_side(self, point_a, point_b):
        "| AB | = √((х1 - х2)² + (у1 - у2)²)."
        return math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)

    # площадь
    def square(self):
        half_p = self.perimeter() / 2
        return math.sqrt(half_p * (half_p-self.ab) * (half_p-self.bc) * (half_p-self.ca))

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def height(self, side):
        return self.square() / side


"A(0, 1), B(5, 2), C(9, 1)"
triangle = Triangle((0, 1), (5, 2), (9, 1))
print("P = ", triangle.perimeter())
print("S = ", triangle.square())
print("height1 = ", triangle.height(triangle.ab))
print("height2 = ", triangle.height(triangle.bc))
print("height3 = ", triangle.height(triangle.ca))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapezoid:
    """
    точки в формате A(1, 1), B(2, 4), C(4, 4), D (5, 1)
    """

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.ab = self.calculate_side(a, b)
        self.bc = self.calculate_side(b, c)
        self.cd = self.calculate_side(c, d)
        self.da = self.calculate_side(d, a)

    def calculate_side(self, point_a, point_b):
        "| AB | = √((х1 - х2)² + (у1 - у2)²)."
        return math.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2)
trapezoid = Trapezoid ((1, 1), (2, 4), (4, 4), (5, 1))
print(trapezoid.calculate_side.ab)