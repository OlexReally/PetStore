import pytest
from data.pet.pet_container import *


#fixtures.py
def setup_module(module):
    rabbit = get_rabbit()
    post_add_pet(rabbit.post_pet_xml())


def test_delete_excist():
    rabbit = get_rabbit()
    delete_pet(rabbit.pet_id)
    with pytest.raises(RuntimeError):
        getapi("http://petstore.swagger.io/v2/pet/" + rabbit.pet_id)


def test_delete_noexcist():
    rabbit = get_rabbit()
    with pytest.raises(RuntimeError):
        delete_pet(rabbit.pet_id)