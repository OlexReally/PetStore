from lxml import etree
from enum import Enum
from api_functional.rest_request.connector import Connector
from api_functional.pet_func.pet import Pet
from lxml import objectify
from api_functional.pet_func.pet_status import PetStatus
import logging as log

class PetDriver:
    __URL = "v2/pet/"
    __HEADERS_SINGLE = {'accept': 'application/xml'}
    __HEADERS_UPDATE = {'accept': 'application/xml', 'Content-Type': 'application/x-www-form-urlencoded'}
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

    def __init__(self, url):
        self.__URL = url + self.__URL

    def create_pet(self, obj):
        log.info("THIS IS INFO")
        log.warning("THIS IS WARNING")
        log.critical("THIS IS CRITICAL")

        new_xml = etree.tostring(obj, pretty_print=True, xml_declaration=True)
        connect = Connector()
        answer = connect.post(self.__URL, new_xml, headers=self.__HEADERS_DOUBLE)

        return Pet(objectify.fromstring(answer.content))

    def update(self, id_, name: str=None, status: PetStatus=None):
        connect = Connector()
        data = None
        if name is not None:
            data = 'name=' + name
        if status is not None and data is None:
            data = 'status=' + status.value
        if status is not None:
            data = data + '&status=' + status.value
        connect.post((self.__URL + str(id_)), data, self.__HEADERS_UPDATE)

    def get_pet(self, id_):
        data_xml = Connector.get(self.__URL+str(id_), self.__HEADERS_SINGLE).content
        return Pet(objectify.fromstring(data_xml))

    def delete_pet(self, id_):
        return Connector.delete(self.__URL+str(id_), self.__HEADERS_SINGLE)

    def get_xml(self, id_):
        return Connector.get(url=(self.__URL + str(id_)), headers=self.__HEADERS_SINGLE).content
