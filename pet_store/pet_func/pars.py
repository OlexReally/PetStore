"""
    Contains Parser for XML document
"""
from lxml import objectify


class Parser:
    """
        Class, which contains static method's for parsing XML document
    """
    @staticmethod
    def get_id_from_xml(data_xml):
        """
        Static method, which Pars XML and return Pet ID

        :param data_xml: XML document
        :return: ID
        """
        objc = objectify.fromstring(data_xml)
        return objc.id.text

    @staticmethod
    def get_name_from_xml(data_xml):
        """
        Static method, which Pars XML and return Pet Name

        :param data_xml: XML document
        :return: Name
        """
        objc = objectify.fromstring(data_xml)
        return objc.name.text

    @staticmethod
    def get_status_xml(data_xml):
        """
        Static method, which Pars XML and return Pet status

        :param data_xml: XML document
        :return: Status
        """
        objc = objectify.fromstring(data_xml)
        return objc.status.text
