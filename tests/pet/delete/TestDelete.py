from api_functional.pet_func.pet import Pet
from tests.conftest import HOST_URL
from data.pet.pet_container import cat_pet
from api_functional.pet_func.pet_functional import PetDriver
from api_functional.rest_request.connector import Connector


def test_delete_existing_pet():
    pet_driver = PetDriver(HOST_URL)
    pet = Pet(cat_pet())
    pet = PetDriver.create_pet(cat_pet())

    PetDriver.delete_pet(pet.id)
