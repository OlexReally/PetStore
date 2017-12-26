"""
    Contains class Pet
"""
import logging as log
from pet_store.pet_func.pet_status import PetStatus


class Pet:
    """
    Contains pet instance.

    Attributes:
        __pet_id        Pet ID, number
        __pet_name      Name of pet
        __pet_status    Pet status (available,  pending, sold)
    """
    def __init__(self, pet_object):
        """
        Create pet instance

        :param pet_object: objectify pet object, parsed from .xml file or server's response
        """
        self.__pet_init(pet_object)
        log.info("New pet instance created")
        log.debug("New pet instance created with id=%s and name=%s", self.id, self.name)

    def __pet_init(self, pet_object):
        """
        Method for init pet's attributes

        :param pet_object: objectify pet object, parsed from .xml file or server's response
        """
        self.__pet_id = pet_object.id.text
        self.__pet_name = pet_object.name.text
        self.__pet_status = self.__pet_status_init(pet_object.status.text)

    def __pet_status_init(self, text):
        """
        Init pet status

        :param text: pet status in text
        :return: Pet status
        """
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
