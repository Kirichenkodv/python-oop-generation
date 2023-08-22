class Pet:
    names = []

    @classmethod
    def first_pet(cls):
        return cls.names
    
    @classmethod
    def last_pet(cls):
        return cls.names
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.names)
    
    def __init__(self, name):
        self.name = name
        Pet.names.append(self)
        


# INPUT DATA:

# TEST_1:
print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

# TEST_2:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# # TEST_3:
# names = ['Mia', 'Tutti', 'Erin', 'Loki', 'Kelly', 'Hussy', 'Abbey', 'Luna', 'Isha', 'Diva', 'Brandy', 'Petra', 'Mandy', 'Baby', 'Caitlyn', 'Taffy', 'Odie', 'Roxxy', 'Gabby', 'Shelby', 'Dolly', 'Ashley', 'Vanilla', 'Cori']

# for name in names:
#     pet = Pet(name)

# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())

# # TEST_4:
# pet = Pet('Кемаль')

# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())

# # TEST_5:
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
# pet4 = Pet('Ratchet')
# pet5 = Pet('Ratchet')

# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())
