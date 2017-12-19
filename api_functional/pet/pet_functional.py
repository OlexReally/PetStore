from lxml import objectify
from api_functional.rest_request.connector import *
from data.pet import *


class PetDriver:
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

    def __init__(self, url):
        self.__URL = url + self.__URL  # http://petstore.swagger.io/    +   v2/pet/

    def update_full(self, pet):  # put
        pass

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, _id):  # get by id
        pass

    def update_by_id(self, _id):  # post by id
        pass

    def delete(self, _id):  # delete
        Connector.delete(self.__URL+_id, self.__HEADERS_SINGLE)

    def upload_image(self, pet):  # post uploadImage
        pass