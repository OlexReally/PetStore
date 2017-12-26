from data.pet.pet_container import rabbit_pet
from data.pet.pet_container import dog_pet
from data.pet.pet_container import cat_pet
from pet_store.pet_func.pet_functional import PetDriver
from pet_store.pet_func.pet_status import PetStatus
from tests.conftest import HOST_URL
import pytest


def test_pet(pet_provider):
    pet_driver = PetDriver(HOST_URL)
    pet = pet_driver.create_pet(pet_provider)  # , "rabbit007", status=PetStatus.AVAILABLE)

    pet_driver.update(pet.id, name="murchik", status=PetStatus.SOLD)
    pet = pet_driver.get_pet(pet.id)

    pet_driver.delete_pet(pet.id)
    with pytest.raises(RuntimeError) as info:
        pet_driver.get_pet(pet.id)

    assert str(info.value) == "Requested data not found"
