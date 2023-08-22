from functools import singledispatchmethod
import datetime



class BirthInfo:
    @singledispatchmethod
    @classmethod
    def class_method(cls, arg):
        print('Базовая реализация метода класса')

    @class_method.register(str)                               # перегружаем метод класса
    @classmethod
    def _class_method(cls, arg):
        print('Реализация метода класса для строкового аргумента')





