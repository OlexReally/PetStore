import pytest
from data.pet.pet_container import *
from api_functional.pet.pet import *
from api_functional.tool.xml_tool import *
from tests.conftest import *
from api_functional.pet.pet_functional import *


@pytest.fixture()
def pet_data_provider():
    xml_tool = XML_Tool()
    return xml_tool.get_xml_from_file(file='D:/PetStore/api_functional/tool/rabbit.xml')


def test_delete_excist(pet_data_provider, url_provider):
    #pet = pet_rabbit().post_pet_xml()
    #rabbit = pet_data_provider
    #xml_tool = XML_Tool()
    #data = xml_tool.get_xml_from_file(file='D:/PetStore/api_functional/tool/rabbit.xml')
    #url = "http://petstore.swagger.io/"
    obj = objectify.fromstring(pet_data_provider)
    rabbit = Pet(url=url_provider, pet_object=obj)
    # TODO write delete
    pet_driver = PetDriver(url_provider)
    pet_driver.delete(rabbit.id)
    # rabbit.delete()
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    #delete_pet(rabbit.pet_id)
    with pytest.raises(RuntimeError):
        Connector.get("http://petstore.swagger.io/v2/pet/" + rabbit.id, __HEADERS_SINGLE)


def test_delete_noexcist_negative(pet_data_provider, url_provider):
    url = "http://petstore.swagger.io/"
    obj = objectify.fromstring(pet_data_provider)
    rabbit = Pet(url=url_provider, pet_object=obj)
    with pytest.raises(RuntimeError):
        # TODO write delete
        pass
        # rabbit.delete()
