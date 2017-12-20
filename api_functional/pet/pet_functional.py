from lxml import objectify
from api_functional.rest_request.connector import *
from api_functional.tool.xml_tool import XML_Tool
from data.pet import *


class PetDriver:
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/x-www-form-urlencoded'}

    def __init__(self, url):
        self.__URL = url + self.__URL  # http://petstore.swagger.io/    +   v2/pet/

    def update_full(self, _id):  # put
        pass

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, _id):  # get by id
        pass

    def update_by_id(self, _id, name=0, status=0):  # post by id
        Connect = Connector()
        if name != 0 and status != 0:
            Connect.post((self.__URL+str(_id)), ('name='+name+'&status='+status), self.__HEADERS_DOUBLE)
        elif name != 0:
            Connect.post((self.__URL+str(_id)), ('name=' + name), self.__HEADERS_DOUBLE)
        else:
            Connect.post((self.__URL+str(_id)), ('&status=' + status), self.__HEADERS_DOUBLE)

        tool = XML_Tool()
        return tool.get_xml_from_webapi(_id)


    def delete(self):  # delete
        Connector.delete(self.__URL+self.id, self.__HEADERS_SINGLE)

    def upload_image(self, pet):  # post uploadImage
        pass