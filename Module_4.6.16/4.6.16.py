class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode

    @property
    def r(self):
        return int(self._hexcode[:2], 16)

    @property
    def g(self):
        return int(self._hexcode[2:4], 16)

    @property
    def b(self):
        return int(self._hexcode[4:], 16)

    @property
    def hexcode(self):
        return (hex(self.r) + hex(self.g) + hex(self.b)[1:]).replace("x","").upper()

    @hexcode.setter
    def hexcode(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b




# INPUT DATA:

# TEST_1:
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_2:
color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_3:
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print()

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_4:
hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1