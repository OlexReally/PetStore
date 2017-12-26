"""
Provides pet objects, from .xml files
"""
import os
from lxml import objectify

CURRENT_PATH = os.path.dirname(os.path.abspath(os.path.join(__file__)))

CAT_PATH = CURRENT_PATH + r'\cat.xml'
DOG_PATH = CURRENT_PATH + r'\dog.xml'
RABBIT_PATH = CURRENT_PATH + r'\rabbit.xml'
WRONG_PET_PATH = CURRENT_PATH + r'\wrong_pet.xml'


def cat_pet():
    """
    Get cat pet

    :return: objectify of cat.xml
    """
    return objectify.parse(CAT_PATH).getroot()


def dog_pet():
    """
    Get dog pet

    :return: objectify of dog.xml
    """
    return objectify.parse(DOG_PATH).getroot()


def rabbit_pet():
    """
    Get rabbit pet

    :return: objectify of rabbit.xml
    """
    return objectify.parse(RABBIT_PATH).getroot()


def wrong_pet():
    """
    Get wrong pet, for negative testing

    :return: objectify of wrong_pet.xml
    """
    return objectify.parse(WRONG_PET_PATH).getroot()
