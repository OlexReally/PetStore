from lxml import objectify
from api_functional.rest_requests.connector import *
from data.pet import *

# get pet by id
class Pet:
    # __URL = "http://petstore.swagger.io/v2/pet/1111"
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

    def __init__(self, url, pet_object):
        self.__URL = url + self.__URL  # pet.id str(pet_id)
        self.__pet_init(pet_object)

    def __pet_init(self, pet_object):
        self.__pet_id = pet_object.id.text
        self.__pet_category_id = pet_object.category.id.text
        self.__pet_category_name = pet_object.category.name.text
        self.__pet_name = pet_object.name.text
        self.__pet_photo_url = pet_object.photoUrls.photoUrl.text
        self.__pet_tag_id = pet_object.tags.tag.id.text
        self.__pet_tag_name = pet_object.tags.tag.name.text
        self.__pet_status = pet_object.status.text
        pass

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

    def update_full(self, pet):  # put
        pass

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, pet):  # get by id
        pass

    def update_by_id(self, pet):  # post by id
        pass

    def delete(self):  # delete
        Connector.delete(url, self.__H)

    def upload_image(self, pet):  # post uploadImage
        pass
