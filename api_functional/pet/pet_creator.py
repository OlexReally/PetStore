from api_functional.tool.xml_tool import XML_Tool
from api_functional.rest_request.connector import Connector
from api_functional.pet.pars import Parser
from lxml import etree

class Creator:
    __HEADERS_DOUBLE = {'accept': 'application/xml', 'Content-Type': 'application/xml'}
    __URL = 'http://petstore.swagger.io/v2/pet'
    def createPet(self, _id=0, name='string', status='available'):
        tool = XML_Tool()
        dataxml = tool.get_xml_from_file()

        obj = tool.create_objectify(dataxml)
        obj.id = _id
        obj.name = name
        obj.status = status

        newxml = etree.tostring(obj, pretty_print=True, xml_declaration=True)
        Connect = Connector()

        Pars = Parser()
        answer = Connect.post(self.__URL, newxml, headers=self.__HEADERS_DOUBLE)
        return Pars.getID_fromXML(answer.content)
