from api_functional.tool.xml_tool import XML_Tool
from api_functional.rest_request.connector import Connector
from lxml import etree

class Creator:

    def createPet(self, _id=0, name='string', status='available'):
        tool = XML_Tool()
        dataxml = tool.get_xml_from_file()

        obj = tool.create_objectify(dataxml)
        obj.id = _id
        obj.name = name
        obj.status = status

        newxml = etree.tostring(obj, pretty_print=True, xml_declaration=True)
        Connect = Connector()
        return Connect.post('http://petstore.swagger.io/v2/pet', newxml, headers={'accept': 'application/xml',
                                                                                  'Content-Type': 'application/xml'})\
        .content

