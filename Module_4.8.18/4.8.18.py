from functools import singledispatchmethod

class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @format.register(int)
    def _format_int(data):
        print(f"Целое число: {data}")

    @format.register(float)
    def _format_float(data):
        print(f"Вещественное число: {data}")

    @format.register(list)
    def _format_list(data):
        print(f"Элементы списка: {', '.join(map(str, data))}")

    @format.register(tuple)
    def _format_tuple(data):
        print(f"Элементы кортежа: {', '.join(map(str, data))}")

    @format.register(dict)
    def _format_dict(data):
        print(f"Пары словаря: {', '.join(map(str, data.items()))}")






# INPUT DATA:

# TEST_1:
Formatter.format(1337)
Formatter.format(20.77)

# # TEST_2:
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

# # TEST_3:
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

# # # TEST_4:
try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)

# # # TEST_5:
not_supported = [str, type, bool, dict, tuple, list]

for item in not_supported:
    try:
        Formatter.format(item)
    except TypeError as e:
        print(e)