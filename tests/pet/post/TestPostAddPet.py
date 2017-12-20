import pytest
from api_functional.pet_func.pet import Pet
from tests.conftest import HOST_URL
from data.pet.pet_container import rabbit_pet
from data.pet.pet_container import dog_pet
from data.pet.pet_container import cat_pet
from api_functional.pet_func.pet_functional import PetDriver
from api_functional.pet_func.pet_status import PetStatus


def test_add_pet():
    pet_driver = PetDriver(HOST_URL)
    pet_actual = Pet(cat_pet())
    pet_expected = pet_driver.create_pet(cat_pet())

    assert pet_actual.name == pet_expected.name
    assert pet_actual.status == pet_expected.status
