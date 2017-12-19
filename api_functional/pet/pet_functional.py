from lxml import objectify
from api_functional.rest_request.connector import *
from data.pet import *


class PetDriver:
    def update_full(self, pet):  # put
        pass

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, _id):  # get by id
        pass

    def update_by_id(self, _id):  # post by id
        pass

    def delete(self):  # delete
        Connector.delete(self.__URL+self.id, self.__HEADERS_SINGLE)

    def upload_image(self, pet):  # post uploadImage
        pass