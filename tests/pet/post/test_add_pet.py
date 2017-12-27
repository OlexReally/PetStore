import pytest
from pet_store.pet_func.pet import Pet
from pet_store.pet_func.pet_functional import PetDriver
from tests.conftest import HOST_URL


def test_add_pet(pet_provider):
    pet_driver = PetDriver(HOST_URL)
    pet_actual = Pet(pet_provider)
    pet_expected = pet_driver.create_pet(pet_provider)

    assert pet_actual.name == pet_expected.name
    assert pet_actual.status == pet_expected.status


def test_add_pet_negative(wrong_pet_provider):
    pet_driver = PetDriver(HOST_URL)

    with pytest.raises(RuntimeError) as error:
        pet_driver.create_pet(wrong_pet_provider)

    assert str(error.value) == 'Bad Request'


def test_update_pet_negative():
    pet_driver = PetDriver(HOST_URL)

    with pytest.raises(RuntimeError) as error:
        pet_driver.update(id_="qwe")

    assert str(error.value) == 'Requested data not found'
