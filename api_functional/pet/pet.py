from lxml import objectify
from api_functional.rest_request.connector import *
from data.pet import *
from api_functional.pet.pet_functional import *

class Pet:
    def __init__(self, pet_object):
        self.__pet_init(pet_object)

    def __pet_init(self, pet_object):
        self.__pet_id = pet_object.id.text
        self.__pet_name = pet_object.name.text
        self.__pet_status = pet_object.status.text

        # self.__pet_category_id = pet_object.Category.id.text
        # self.__pet_category_name = pet_object.Category.name.text
        # self.__pet_photo_url = pet_object.photoUrls.photoUrl.text
        # self.__pet_tag_id = pet_object.tags.Tag.id.text
        # self.__pet_tag_name = pet_object.tags.Tag.name.text

    @property
    def id(self):
        return self.__pet_id

    @property
    def name(self):
        return self.__pet_name

    @property
    def status(self):
        return self.__pet_status

    def update(self, name=None, status=None):
        if name is not None:
            self.__pet_name = name
        if status is not None:
            self.__pet_status = status
        pdriver = PetDriver()
        pdriver.update(self.id, name, status)

    def get(self):
        pdriver = PetDriver()
        pdriver.get_pet(self.id)

    def delete(self):
        pdriver = PetDriver()
        pdriver.delete_pet(self.id)

    # @property
    # def category_id(self):
    #     return self.__pet_category_id
    #
    # @property
    # def category_name(self):
    #     return self.__pet_category_name
    #
    # @property
    # def photo_url(self):
    #     return self.__pet_photo_url
    #
    # @property
    # def tag_id(self):
    #     return self.__pet_tag_id
    #
    # @property
    # def tag_name(self):
    #     return self.__pet_tag_name
