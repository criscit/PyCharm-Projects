"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел."""


class ComplexNumber:
    real: int
    indeterminate: int

    def __init__(self, real: int, imaginable: int = 0):
        self.real = real
        self.indeterminate = imaginable

    def __str__(self):
        if self.indeterminate > 0:
            return f"{self.real}+{self.indeterminate}i"
        elif self.indeterminate < 0:
            return f"{self.real}{self.indeterminate}i"
        else:
            return f"{self.real}"

    def __add__(self, other: 'ComplexNumber'):
        real = self.real + other.real
        imaginable = self.indeterminate + other.indeterminate
        return ComplexNumber(real, imaginable)

    def __mul__(self, other: 'ComplexNumber'):
        real = self.real * other.real - self.indeterminate * other.indeterminate
        imaginable = self.real * other.indeterminate + self.indeterminate * other.real
        return ComplexNumber(real, imaginable)


"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class CustomZeroDivisionError(Exception):
    pass


def get_numerator():
    return int(input("Введите числитель: "))


def get_denominator():
    value = int(input("Введите знаменатель: "))
    if value == 0:
        raise CustomZeroDivisionError
    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()
        print(f"Результат = {numerator / denominator}")
    except CustomZeroDivisionError:
        print("Вы ввели 0 в качестве знаменателя")
    except KeyboardInterrupt:
        break

"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:
    day: int
    month: int
    year: int

    def __init__(self, date: str):
        date_list = Date.converting(date)
        self.validation(date_list)
        self.day, self.month, self.year = date_list

    @classmethod
    def converting(cls, date: str) -> list:
        return [int(x) for x in date.split("-")]

    @staticmethod
    def validation(date_list: list):
        d, m, y = date_list

        assert len(date_list) == 3, "Неверный формат даты"
        assert 1 <= d <= 31, "Неверный формат дня"
        assert 1 <= m <= 12, "Неверный формат месяца"
        assert len(str(y)) == 4 and y > 0, "Неверный формат года"


"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся."""


class Cell:
    __units: int

    def __init__(self, units: int):
        assert units > 0, "Количество ячеек должно быть больше 0"
        self.__units = units

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        total_units = self.units + other.units
        return Cell(total_units)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        total_units = self.units - other.units
        assert total_units > 0, "Количество ячеек первой клетки меньше количества ячеек второй."
        return Cell(total_units)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        total_units = self.units * other.units
        return Cell(total_units)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        total_units = self.units // other.units
        return Cell(total_units)

    def __str__(self):
        return str(self.__units)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Операции допустимы только между клетками"

    @property
    def units(self):
        return self.__units

    @staticmethod
    def make_order(cell_object: 'Cell', units_per_row: int) -> str:
        items = '*' * cell_object.units
        chunks = [
            items[idx:idx + units_per_row]
            for idx in range(0, len(items), units_per_row)
        ]
        return "\n".join(chunks)


"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):
    _size: float

    def __init__(self, size: float):
        super().__init__(name="Пальто")
        self._size = size

    @property
    def calculate(self) -> float:
        return self._size / 6.5 + 0.5


class Suit(Clothes):
    _height: float

    def __init__(self, height: float):
        super().__init__(name="Костюм")
        self._height = height

    @property
    def calculate(self) -> float:
        return self._height * 2 + 0.3


"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица."""


class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __str__(self):
        return "\n".join(str(row).strip("[]").replace(",", "") for row in self.value)

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])
            if rows_count != len(other.value) or items_count != len(other.value[0]):
                raise IndexError
            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]
            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Разные размерности матриц")
            exit(1)


"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости."""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: старт")

    def stop(self):
        print(f"{self.name}: стоп")

    def turn(self, direction: str):
        print(f"{self.name}: поворот - {direction}")

    def show_speed(self):
        print(f"{self.name}: скорость = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: скорость превышена")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: скорость превышена")


class PoliceCar(Car):
    is_police: bool = True


"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода."""


class Road:
    __mass: float = 25
    _width: float
    _length: float

    def __init__(self, width: float, length: float):
        self._width = width
        self._length = length

    def asphalt_mass(self, depth: float = 1):
        return self._length * self._width * self.__mass * depth / 1000


road = Road(20, 5000)
print(f"{road.asphalt_mass(5)} т")

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""
import time


class TrafficLight:
    __color: str
    __timing: dict
    __next_idx: int = 0

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {"красный": red_time, "желтый": yellow_time, "зеленый": green_time}

    def running(self, color: str):
        if list(self.__timing.keys()).index(color) != self.__next_idx:
            print("Неправильный порядок сигналов")
            exit()
        self.__color = color
        timer = self.__timing[color]
        for second in range(timer):
            print(f"{self} [{second + 1}]")
            time.sleep(1)
        next_idx = self.__next_idx + 1
        self.__next_idx = next_idx if next_idx < len(self.__timing) else 0

    def __repr__(self):
        return f"текущий режим = {self.__color}"


try:
    traffic_light = TrafficLight(3, 2, 3)
    traffic_light.running("красный")
    traffic_light.running("желтый")
    traffic_light.running("зеленый")
    traffic_light.running("красный")
    traffic_light.running("зеленый")
except KeyboardInterrupt:
    print("Exit the program")
