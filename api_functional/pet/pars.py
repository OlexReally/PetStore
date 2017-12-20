from lxml import objectify


class Parser:

    @staticmethod
    def get_id_from_xml(dataxml):
        objc = objectify.fromstring(dataxml)
        return objc.id.text

    @staticmethod
    def get_name_from_xml(dataxml):
        objc = objectify.fromstring(dataxml)
        return objc.name.text

    @staticmethod
    def get_status_xml(dataxml):
        objc = objectify.fromstring(dataxml)
        return objc.status.text
