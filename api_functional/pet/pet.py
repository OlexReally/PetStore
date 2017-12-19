from lxml import objectify
from api_functional.requests.connector import *
from data.pet import *

# get pet by id
class Pet:
    # __URL = "http://petstore.swagger.io/v2/pet/1111"
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}
    __pet_object = None

    def __init__(self, url, pet):
        # http://petstore.swagger.io/   +   v2/pet/
        self.__URL = url + self.__URL + pet.id  # str(pet_id)

        self.__pet_object = self.__pet_init(pet)

        # self.r = get("http://petstore.swagger.io/v2/pet/" + str(pet_id))
        # self.pet_response = get(self.__URL, self.__HEADERS)
        # self.__pet_object = objectify.fromstring(self.pet_response.content)

    def __pet_init(self, pet):
        return objectify.fromstring(get(self.__URL, self.__HEADERS))

    # ------------- getters ----------------
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

    def __add(self, pet):  # post
        objectify.fromstring(get(self.__URL, self.__HEADERS))
        pass

    def update_full(self, pet):  # put
        pass

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, pet):  # get by id
        pass

    def update_by_id(self, pet):  # post by id
        pass

    def delete(self, pet):  # delete
        # delete __pet_object
        pass

    def upload_image(self, pet):  # post uploadImage
        pass
