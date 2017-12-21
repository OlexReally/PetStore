import pytest
from data.pet.pet_container import cat_pet, dog_pet, rabbit_pet, wrong_pet
import logging

LOG_LVL = logging.DEBUG


@pytest.fixture(params=[cat_pet(), dog_pet(), rabbit_pet()])
def pet_provider(request):
    return request.param


@pytest.fixture(params=[wrong_pet()])
def wrong_pet_provider(request):
    return request.param


def pytest_sessionstart():
    log = logging.getLogger()
    out_hdlr = logging.FileHandler('LogPet.log')
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_hdlr.setLevel(LOG_LVL)

    log.addHandler(out_hdlr)
    log.setLevel(LOG_LVL)
