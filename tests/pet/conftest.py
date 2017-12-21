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
    out_hdlr = logging.FileHandler(r"logfile.txt", encoding="utf-8")
    out_hdlr.setFormatter(logging.Formatter(u'# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]'
                                            u'%(message)s'))
    out_hdlr.setLevel(LOG_LVL)

    log.addHandler(out_hdlr)
    log.setLevel(LOG_LVL)


def pytest_runtest_setup(item):
    logging.info("====={}=====".format(item.name))


def pytest_runtest_teardown(item):
    logging.info("====={}=====".format(item.name))