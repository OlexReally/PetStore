from lxml import objectify
from api_functional.rest_request.connector import *
from lxml import etree
from enum import Enum
from api_functional.pet.pars import Parser


class Status(Enum):
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'


class PetDriver:
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_UPDATE = {'accept': 'application/xml', 'Content-Type': 'application/x-www-form-urlencoded'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

    def __init__(self, url):
        self.__URL = url + self.__URL  # http://petstore.swagger.io/    +   v2/pet/

    def create_pet(self, name: str, status: Status):
        path = r'D:\PetStore\api_functional\tool\pet.xml'
        obj = objectify.parse(path).getroot()
        obj.name = name
        obj.status = status.value
        new_xml = etree.tostring(obj, pretty_print=True, xml_declaration=True)
        connect = Connector()

        pars = Parser()
        answer = connect.post(self.__URL, new_xml, headers=self.__HEADERS_DOUBLE)
        return pars.get_id_from_xml(answer.content)

    def update(self, id_, name: str=None, status: Status=None):  # post by id
        connect = Connector()
        data = None
        if name is not None:
            data = 'name=' + name
        if status is not None and data is None:
            data = 'status=' + status.value
        if status is not None:
            data = data + '&status=' + status.value

        return connect.post((self.__URL+str(id_)), data, self.__HEADERS_UPDATE)

    def get_by_status(self, pet):  # get by status
        pass

    def get_by_id(self, _id):  # get by id
        pass

    def get_xml(self, id_):
        return Connector.get(url=(self.__URL + str(id_)), headers=self.__HEADERS_SINGLE).content
