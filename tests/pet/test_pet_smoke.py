from data.pet.pet_container import *
from api_functional.pet_func.pet_functional import PetDriver
from api_functional.pet_func.pet_functional import PetStatus
from tests.conftest import HOST_URL


def test_pet():
    # pet_func = Pet(cat_pet())
    #print(cat_pet())
    pet_driver = PetDriver(HOST_URL)
    status = PetStatus
    pet = pet_driver.create_pet(cat_pet(), "rabbit007", status=status.AVAILABLE)
    print(pet.id)
    print(pet.name)
    print(pet.status)
