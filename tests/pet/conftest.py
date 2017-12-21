import pytest
from data.pet.pet_container import cat_pet, dog_pet, rabbit_pet, wrong_pet


@pytest.fixture(params=[cat_pet(), dog_pet(), rabbit_pet()])
def pet_provider(request):
    return request.param


@pytest.fixture(params=[wrong_pet()])
def wrong_pet_provider(request):
    return request.param
