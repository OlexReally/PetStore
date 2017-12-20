from api_functional.tool.xml_tool import XML_Tool


class Parser:

    def getID_fromXML(self, dataxml):
        tool = XML_Tool()
        objc = tool.create_objectify(dataxml)
        return objc.id.text

    def getName_fromXML(self, dataxml):
        tool = XML_Tool()
        objc = tool.create_objectify(dataxml)
        return objc.name.text

    def getStatus_fromXML(self, dataxml):
        tool = XML_Tool()
        objc = tool.create_objectify(dataxml)
        return objc.status.text
