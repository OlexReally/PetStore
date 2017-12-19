from lxml import objectify
from api_functional.rest_request.connector import *
from data.pet import *

# get pet by id
class Pet:
    # __URL = "http://petstore.swagger.io/v2/pet/1111"
    # __URL = "v2/pet/"
    # __HEADERS_SINGLE = {'accept': 'application/xml'}
    # __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

    def __init__(self, url, pet_object):
        self.__URL = url + self.__URL  # pet.id str(pet_id)
        self.__pet_init(pet_object)

    def __pet_init(self, pet_object):
        #print("_______________\n" + pet_object.category.id.text + "\n______________")

        self.__pet_id = pet_object.id.text
        self.__pet_category_id = pet_object.Category.id.text
        self.__pet_category_name = pet_object.Category.name.text
        self.__pet_name = pet_object.name.text
        self.__pet_photo_url = pet_object.photoUrls.photoUrl.text
        self.__pet_tag_id = pet_object.tags.Tag.id.text
        self.__pet_tag_name = pet_object.tags.Tag.name.text
        self.__pet_status = pet_object.status.text



    # ------------- getters ----------------
    @property
    def id(self):
        return self.__pet_id

    @property
    def category_id(self):
        return self.__pet_category_id

    @property
    def category_name(self):
        return self.__pet_category_name

    @property
    def name(self):
        return self.__pet_name

    @property
    def photo_url(self):
        return self.__pet_photo_url

    @property
    def tag_id(self):
        return self.__pet_tag_id

    @property
    def tag_name(self):
        return self.__pet_tag_name

    @property
    def status(self):
        return self.__pet_status

    # def id_tag(self):
    #     return self.response_object.id.text
    #
    # def name_tag(self):
    #     return self.response_object.name.text
    #
    # def photourls_tag(self):
    #     return self.response_object.photoUrls.text
    #
    # def status_tag(self):
    #     return self.response_object.status.text
    #
    # def tags_tag(self):
    #     return self.response_object.tags.text
    # ------------- getters ----------------

    # post not need
    # def __add(self, pet):  # post
    #     objectify.fromstring(get(self.__URL, self.__HEADERS))
    #     pass
