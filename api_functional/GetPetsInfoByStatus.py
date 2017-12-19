from api_functional.requests.request import getapi
from lxml import etree


class GetPetsInfoByStatus:
    def __init__(self, status, tag):
        self.answer = getapi("http://petstore.swagger.io/v2/pet/findByStatus?status=" + str(status))
        self.tag = tag

    def get_tag_list(self):
        tree = etree.XML(self.answer.content)
        Pets = tree.xpath('.//Pet/' + self.tag)
        for pet in Pets:
            print(self.tag + ' = ', [pet.text])
