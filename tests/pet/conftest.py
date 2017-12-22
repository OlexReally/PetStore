import pytest
from data.pet.pet_container import cat_pet, dog_pet, rabbit_pet, wrong_pet
import logging
import traceback

LOG_LVL = logging.DEBUG
PASS = 32
FAIL = 33
logging.addLevelName(PASS, 'PASS')
logging.addLevelName(FAIL, 'FAIL')


def passed(self, message, *args, **kws):
    self.log(PASS, message, *args, **kws)


def failed(self, message, *args, **kws):
    self.log(FAIL, message, *args, **kws)


logging.Logger.passed = passed
logging.Logger.failed = failed
log = logging.getLogger()


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
    log.info(item._obj.__doc__)


def pytest_runtest_teardown(item):
    logging.info("====={}=====".format(item.name))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #pytest_plugins = 'allure.pytest_plugin'

    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        tb = "".join(traceback.format_tb(call.excinfo.tb)[-5:])
        if call.excinfo.type is not AssertionError:
            log.error("Error \"{}\" occurred! Traceback: \n{}".format(call.excinfo.typename, tb))
        else:
            log.failed("Test {} failed! \n{}".format(item.name, tb))

    elif rep.passed and rep.when == "call":
        log.passed("Test {} passed.".format(item.name))