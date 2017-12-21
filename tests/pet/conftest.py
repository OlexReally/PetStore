import pytest
from data.pet.pet_container import cat_pet, dog_pet, rabbit_pet, wrong_pet
# from lxml import objectify
#
# CAT_PATH = '/PetStore/data/pet_func/rabbit.xml'
# DOG_PATH = '/PetStore/data/pet_func/dog.xml'
# RABBIT_PATH = '/PetStore/data/pet_func/rabbit.xml'
#
# # tests/pet_func/conftest.py
#
#
# # pet_obj = objectify.fromstring(pet_data_provider)
# @pytest.fixture()
# def pet_rabbit_provider():
#     # xml_tool = XML_Tool()
#     return 0  # xml_tool.get_xml_from_file(file=RABBIT_PATH)
#
#
# @pytest.fixture()
# def pet_dog_provider():
#     # xml_tool = XML_Tool()
#     return 0  # xml_tool.get_xml_from_file(file=DOG_PATH)
#
#
# @pytest.fixture()
# def pet_cat_provider():
#     #xml_tool = XML_Tool()
#     return 0  # xml_tool.get_xml_from_file(file=CAT_PATH)


@pytest.fixture(params=[cat_pet(), dog_pet(), rabbit_pet()])
def pet_provider(request):
    return request.param


@pytest.fixture(params=[wrong_pet()])
def wrong_pet_provider(request):
    return request.param
