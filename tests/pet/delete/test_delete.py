from api_functional.pet_func.pet import Pet
from tests.conftest import HOST_URL
import pytest
from data.pet.pet_container import cat_pet
from api_functional.pet_func.pet_functional import PetDriver


def test_delete_existing_pet(pet_provider):
    pet_driver = PetDriver(HOST_URL)
    pet = pet_driver.create_pet(pet_provider)

    assert pet_driver.delete_pet(pet.id).status_code == 200


def test_delete_not_existing_pet(pet_provider):
    pet_driver = PetDriver(HOST_URL)
    pet = pet_driver.create_pet(pet_provider)
    pet_driver.delete_pet(pet.id)

    with pytest.raises(RuntimeError) as info:
        pet_driver.delete_pet(pet.id)

    assert str(info.value) == 'Requested data not found'
