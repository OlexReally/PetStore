import pytest
from data.pet.pet_container import *
from api_functional.pet_func.pet import *
from api_functional.tool.xml_tool import *
from tests.conftest import *
from api_functional.pet_func.pet_functional import *
from tests.pet.conftest import *


def test_delete_exist(pet_rabbit_provider):
    pet = Pet(pet_rabbit_provider)  # pet_func instance create
    pet_driver = PetDriver(HOST_URL)  # pet_func driver create with HOST_URL
    # pet_driver.delete(rabbit.id) TODO change delete

    __HEADERS_SINGLE = {'accept': 'application/xml'}
    with pytest.raises(RuntimeError):
        # TODO need replace to pet_driver.get(pet_func.id), it should give exception
        Connector.get(HOST_URL + pet.id, __HEADERS_SINGLE)


def test_delete_not_exist_negative(pet_rabbit_provider):
    pet = Pet(pet_rabbit_provider)  # pet_func instance create
    pet_driver = PetDriver(HOST_URL)  # pet_func driver create with HOST_URL
    with pytest.raises(RuntimeError):
        # TODO write delete
        pass
        # rabbit.delete()
