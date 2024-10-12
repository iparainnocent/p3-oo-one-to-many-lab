import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Fido", "dog", None)  # Initialize with None or a valid owner
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)  # Now this should work
    assert pet.name == "Clifford"
    assert pet.pet_type == "dog"
    assert pet.owner == owner  # Optional: check if the owner is set correctly
    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    owner = Owner("Jim")

    pet1 = Pet("Whiskers", "cat", owner)
    pet2 = Pet("Jerry", "reptile", owner)

    assert pet1.name == "Whiskers"
    assert pet1.pet_type == "cat"
    assert pet1.owner == owner

    Pet.all = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    assert owner.pets() == [pet1, pet2]

    Pet.all = []

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat", owner)
    owner.add_pet(pet)

    assert pet in owner.pets()

    assert pet.owner == owner
    assert owner.pets() == [pet]

    Pet.all = []

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    owner = Owner("Jim")
    with pytest.raises(TypeError):
        owner.add_pet("Not a pet")

    Pet.all = []

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)

    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    owner.add_pet(pet4)

    
    assert owner.get_sorted_pets() == [pet2, pet1, pet4, pet3]