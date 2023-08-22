class QuadraticPolynomial:

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string):
        lst = [float(x) for x in string.split(" ")]
        return cls(*lst)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c






# INPUT DATA:

# TEST_1:
polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)

# # TEST_3:
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)

# # TEST_4:
# polynom = QuadraticPolynomial.from_str('-19 40 148')

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

# # TEST_5:
# polynom = QuadraticPolynomial.from_iterable([25, 132, -18])

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

# # TEST_6:
# polynom = QuadraticPolynomial.from_iterable([2.5, 13.2, -1.8])

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

