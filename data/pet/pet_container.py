import os
from lxml import objectify

CURRENT_PATH = os.path.dirname(os.path.abspath(os.path.join(__file__)))

CAT_PATH = CURRENT_PATH + r'\cat.xml'
DOG_PATH = CURRENT_PATH + r'\dog.xml'
RABBIT_PATH = CURRENT_PATH + r'\rabbit.xml'


def cat_pet():
    return objectify.parse(CAT_PATH).getroot()


def dog_pet():
    return objectify.parse(DOG_PATH).getroot()


def rabbit_pet():
    return objectify.parse(RABBIT_PATH).getroot()


# def pet_rabbit():
#     return PetProvider(pet_id="1112",
#                        pet_category_id="345",
#                        pet_category_name="home",
#                        pet_name="rabbit",
#                        pet_photo_url="string",
#                        pet_tag_id="543",
#                        pet_tag_name="tag",
#                        pet_status="available")
#
#
# def pet_dog():
#     return PetProvider(pet_id="1113",
#                        pet_category_id="346",
#                        pet_category_name="yard",
#                        pet_name="dog",
#                        pet_photo_url="string",
#                        pet_tag_id="544",
#                        pet_tag_name="tag",
#                        pet_status="available")
#
#
# def pet_cat():
#     return PetProvider(pet_id="1114",
#                        pet_category_id="347",
#                        pet_category_name="home",
#                        pet_name="rabbit",
#                        pet_photo_url="string",
#                        pet_tag_id="545",
#                        pet_tag_name="tag",
#                        pet_status="available")
