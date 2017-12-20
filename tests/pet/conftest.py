import pytest
from lxml import objectify

CAT_PATH = '/PetStore/data/pet/rabbit.xml'
DOG_PATH = '/PetStore/data/pet/dog.xml'
RABBIT_PATH = '/PetStore/data/pet/rabbit.xml'

# tests/pet/conftest.py


# pet_obj = objectify.fromstring(pet_data_provider)
@pytest.fixture()
def pet_rabbit_provider():
    # xml_tool = XML_Tool()
    return 0  # xml_tool.get_xml_from_file(file=RABBIT_PATH)


@pytest.fixture()
def pet_dog_provider():
    # xml_tool = XML_Tool()
    return 0  # xml_tool.get_xml_from_file(file=DOG_PATH)


@pytest.fixture()
def pet_cat_provider():
    #xml_tool = XML_Tool()
    return 0  # xml_tool.get_xml_from_file(file=CAT_PATH)
