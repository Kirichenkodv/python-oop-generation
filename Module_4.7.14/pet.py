class Pet:
    names = []

    def __init__(self, name):
        self.name = name
        self.names.append(name)

    @classmethod
    def first_pet(cls):
        return None if not cls.names else cls.names[0]
    
    @classmethod
    def last_pet(cls):
        return None if not cls.names else cls.names[-1]
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.names)
    

    
    






pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
