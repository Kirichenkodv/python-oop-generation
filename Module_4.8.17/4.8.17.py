from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")
    
    @neg.register(int)
    def _neg_int(data):
        return - data
    
    @neg.register(float)
    def _neg_float(data):
        return - data
    
    @neg.register(bool)
    def _neg_bool(data):
        return not data
    
    








# INPUT DATA:

# TEST_1:
print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

# TEST_2:
try:
    Negator.neg('number')
except TypeError as e:
    print(e)

# TEST_3:
not_supported = [[1, 2, 3], (4, 5, 6), {1: 'one'}, {10, 11, 12}, 'Timothy John «Tim» Berners-Lee']

for item in not_supported:
    try:
        Negator.neg(item)
    except TypeError as e:
        print(e)