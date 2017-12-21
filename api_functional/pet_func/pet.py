#from lxml import objectify
#from api_functional.rest_request.connector import *
#from data.pet import *
from api_functional.pet_func.pet_status import PetStatus
# from api_functional.pet_func.pet_functional import PetDriver
from tests.conftest import HOST_URL


class Pet:
    def __init__(self, pet_object):
        self.__pet_init(pet_object)

    def __pet_init(self, pet_object):
        self.__pet_id = pet_object.id.text
        self.__pet_name = pet_object.name.text
        self.__pet_status = self.__pet_status_init(pet_object.status.text)

    def __pet_status_init(self, text):
        status = PetStatus
        if text == status.AVAILABLE.value:
            return status.AVAILABLE
        elif text == status.PENDING.value:
            return status.PENDING
        else:
            return status.SOLD

    @property
    def id(self):
        return self.__pet_id

    @property
    def name(self):
        return self.__pet_name

    @property
    def status(self):
        return self.__pet_status
