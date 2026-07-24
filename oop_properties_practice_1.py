"""
Добавьте в класс Product геттер count_available. Он должен возвращать количество единиц товара, доступных для продажи.

Создайте инстанс scanner с инвентарным номером "scanner_3492", общим количеством единиц 19 и количеством зарезервированных единиц 3.
"""


class Product:
    def __init__(self, number, count_total, count_reserved):
        self.number = number  # Инвентарный номер товара
        self.count_total = count_total  # Общее количество единиц товара на складе
        self.count_reserved = count_reserved  # Количество зарезервированных единиц

    @property
    def count_avaliable(self):
        return f"Количество товаров, доступных для продажи: {self.count_total - self.count_reserved}"


scanner = Product("scanner_3492", 19, 3)
# print(scanner.count_avaliable)

"""
В классе Product вместо поля number заведите геттер и сеттер с именем number. 
Чтобы не было конфликта имен, само поле сделайте приватным (переименуйте в _number).

Геттер number должен выводить в консоль строку "Getting value" и затем возвращать значение поля.

Сеттер number должен выводить в консоль "Setting value VAL" (здесь вместо VAL должно быть выведено реальное присваиваемое значение) и затем проверять, что присваиваемый номер состоит только из букв латинского алфавита и цифр. 
Если это не так, сеттер должен бросать исключение ValueError.

Добейтесь того, чтобы сеттер срабатывал даже в методе-инициализаторе.

Проанализируйте консольный вывод: удостоверьтесь, что сеттер объекта headphones вызвался дважды.
"""


class Product:
    def __init__(self, number, count_total, count_reserved):
        self.number = number
        self.count_total = count_total
        self.count_reserved = count_reserved

    @property
    def number(self):
        return f"Getting value {self._number}"

    @number.setter
    def number(self, number):
        if number.isalnum() and number.isascii():
            self._number = number
        else:
            raise ValueError("Номер должен содержать цифры или латиницу!")


headphones = Product("headphones", 5, 0)
x = headphones.number
# print(x)
headphones.number = "headphones001"
# print(headphones.number)


"""
Имплементируйте класс Color, который принимает в инициализаторе 3 значения: r, g, b.

Добавьте в класс свойство hex, которое бы возвращало шестнадцатеричное представление цвета. 
Можете воспользоваться вспомогательной функцией rgb_to_hex().

Запретите удалять свойство hex: при попытке удаления должно генерироваться исключение AttributeError с текстом "Hex attribute can not be deleted".
"""


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    @hex.deleter
    def hex(self):
        raise AttributeError("Hex attribute can not be deleted")


c = Color(169, 3, 252)
# print(c.hex)

# try:
#     del c.hex
# except AttributeError as e:
# print(f"Deleting hex: {e}")


"""
Реализуйте класс Circle, в инициализатор которого передаются координаты x,y и радиус.

Напишите свойство r для радиуса с проверкой, он не может быть отрицательным. В таком случае генерируйте ValueError.

Добавьте в класс свойства area и circumference для расчета площади круга и длины окружности.
"""


from math import pi


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        if r >= 0:
            self._r = r
        else:
            raise ValueError("Радиус не может быть отрицательным!")

    @property
    def area(self):
        return pi * self._r**2

    @property
    def circumference(self):
        return 2 * pi * self._r


c = Circle(5, 2.01, 6)
print(c.area)
print(c.circumference)

# Проверяем защиту от отрицательного радиуса при изменении
try:
    c.r = -3
except ValueError as e:
    print(f"Ошибка при изменении: {e}")

# Проверяем защиту от отрицательного радиуса при инициализации
try:
    wrong_circle = Circle(0, 0, -10)
except ValueError as e:
    print(f"Ошибка при создании: {e}")
