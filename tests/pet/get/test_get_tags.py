from pet_store.pet_func.pet import *
from pet_store.pet_func.pet_functional import PetDriver


def test_get_pet(pet_provider):
    pet_driver = PetDriver(HOST_URL)
    pet_actual = Pet(pet_provider)
    pet_expected = pet_driver.get_pet(pet_driver.create_pet(pet_provider).id)

    assert pet_actual.name == pet_expected.name
    assert pet_actual.status == pet_expected.status
