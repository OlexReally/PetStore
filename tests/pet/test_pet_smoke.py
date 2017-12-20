from data.pet.pet_container import rabbit_pet
from data.pet.pet_container import dog_pet
from data.pet.pet_container import cat_pet
from api_functional.pet_func.pet_functional import PetDriver
from api_functional.pet_func.pet_status import PetStatus
from tests.conftest import HOST_URL
import pytest


def test_pet():
    pet_driver = PetDriver(HOST_URL)
    pet = pet_driver.create_pet(cat_pet())  # , "rabbit007", status=PetStatus.AVAILABLE)
    print(pet.id)
    print(pet.name)
    print(pet.status.value)

    pet_driver.update(pet.id, name="murchik", status=PetStatus.SOLD)
    pet = pet_driver.get_pet(pet.id)
    print(pet.id)
    print(pet.name)
    print(pet.status.value)

    pet_driver.delete_pet(pet.id)
    with pytest.raises(RuntimeError) as info:
        pet_driver.get_pet(pet.id)

    print(info)
