import logging
import sys
from tests.conftest import LOG_LVL


def my_logger():
    log = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_hdlr.setLevel(LOG_LVL)

    log.addHandler(out_hdlr)
    log.setLevel(LOG_LVL)
    return log
