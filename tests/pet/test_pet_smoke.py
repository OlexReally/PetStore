from data.pet.pet_container import *
from api_functional.pet.pet_functional import *
from tests.conftest import *
from api_functional.pet import *


def test_pet():
    pet = Pet(cat_pet())
