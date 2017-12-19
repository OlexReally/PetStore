import pytest
from data.pet.pet_container import *
from api_functional.pet.pet import *
from api_functional.tool.xml_tool import *


# @pytest.fixture()
# def pet_data_provider(request):
#     return pet_rabbit().post_pet_xml()


def test_delete_excist():
    #pet = pet_rabbit().post_pet_xml()
    #rabbit = pet_data_provider
    xml_tool = XML_Tool()
    data = xml_tool.get_xml_from_file(file='D:/PetStore/api_functional/tool/rabbit.xml')
    url = "http://petstore.swagger.io/"
    obj = objectify.fromstring(data)
    rabbit = Pet(url=url, pet_object=obj)
    rabbit.delete()
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    #delete_pet(rabbit.pet_id)
    with pytest.raises(RuntimeError):
        Connector.get("http://petstore.swagger.io/v2/pet/" + rabbit.id, __HEADERS_SINGLE)

#
# def test_delete_noexcist():
#     rabbit = get_rabbit()
#     with pytest.raises(RuntimeError):
#         delete_pet(rabbit.pet_id)