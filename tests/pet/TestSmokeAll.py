import pytest
from data.pets import *
from api_functional.Request import *
from api_functional.PetGetTags import *


def test_first():
    rabbit = get_rabbit()

    with pytest.raises(RuntimeError):
        getapi("http://petstore.swagger.io/v2/pet/"+rabbit.pet_id)

    post_add_pet(get_rabbit().post_pet_xml())

    getapi("http://petstore.swagger.io/v2/pet/" + rabbit.pet_id)

    delete_pet(rabbit.pet_id)

    with pytest.raises(RuntimeError):
        getapi("http://petstore.swagger.io/v2/pet/"+rabbit.pet_id)