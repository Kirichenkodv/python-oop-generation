# class Processor:
#     @staticmethod
#     def process(data):
#         if isinstance(data, (int, float)):
#             return data * 2
#         elif isinstance(data, str):
#             return data.upper()
#         elif isinstance(data, list):
#             return sorted(data)
#         elif isinstance(data, tuple):
#             return tuple(sorted(data))
#         raise TypeError('Аргумент переданного типа не поддерживается')

from functools import singledispatchmethod 

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register(int)
    def _process_int(data):
        return data * 2
    
    @process.register(float)
    def _process_float(data):
        return data * 2
    
    @process.register(str)
    def _process_str(data):
        return data.upper()
    
    @process.register(tuple)
    def _process_tuple(data):
        return sorted(data)
    
    @process.register(list)
    def _process_list(data):
        return sorted(data)
    


    



# INPUT DATA:

# TEST_1:
print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))



#TEST_2:
# try:
#     Processor.process({1, 2, 3})
# except TypeError as e:
#     print(e)

# # TEST_3:
print(Processor.process(100))
print(Processor.process(True))
print(Processor.process(False))
print(Processor.process(55.2))
print(Processor.process('beegeek_stepik_python'))
print(Processor.process((23, 56, 1, 3, -3, 0, 4, 10, 11, -90)))
print(Processor.process([10, 2, 11, 9, 5, -4, -90]))

# # TEST_4:
objects = [None, {1, 2, 3}, {1: 'one', 2: 'two'}]

for obj in objects:
    try:
        Processor.process(obj)
    except TypeError as e:
        print(e)