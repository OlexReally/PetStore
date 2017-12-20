import pytest
from tests.conftest import *
from tests.pet.conftest import *

def test_obj():
    path = r'\PetStore\api_functional\tool\pet.xml'
    obj = objectify.parse(path).getroot()
    print(obj.name.text)

# def test_url(url_provider):
#     print(url_provider)

