from functools import singledispatchmethod

class IPAddress:
    @singledispatchmethod
    def __init__(self, data):
        raise TypeError("Аргумент не поддурживается")
    
    @__init__.register
    def _init_str(self, data : str):
        self.data = data

    @__init__.register
    def _init_list(self, data : list):
        self.data = (".").join(map(str, data))

    @__init__.register
    def _init_tuple(self, data : tuple):
        self.data = (".").join(map(str, data))

    def __str__(self):
        return self.data
    
    def __repr__(self):
        return f"IPAddress('{self.data}')"
    




# INPUT DATA:

# TEST_1:
ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

# TEST_2:
ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

# TEST_3:
ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))

# TEST_4:
addresses = [(189, 26, 106, 172), '97.248.190.45', '162.149.247.52', (160, 73, 135, 188), (216, 2, 39, 172),
             (31, 27, 97, 53), '95.233.16.231', (0, 19, 242, 236), (1, 166, 90, 22), '135.23.153.66', '235.99.24.247',
             '217.104.124.203', (99, 138, 21, 145), (231, 214, 91, 158), (158, 87, 228, 213), (32, 248, 59, 101),
             '244.236.12.239', '31.201.10.112', '68.206.225.207', '93.212.255.61']

for address in addresses:
    ip = IPAddress(address)
    print(repr(ip))