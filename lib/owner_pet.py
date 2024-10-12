class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    def __init__(self, name, pet_type, owner):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
    

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list to hold pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added.")
        self._pets.append(pet)  # Add the pet to the owner
    
    def pets(self):
        return self._pets  # Return the list of pets
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)