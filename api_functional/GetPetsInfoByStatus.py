from api_functional.rest_request.request import getapi
from lxml import etree


def get_tag_list(status, tag):
    answer = getapi("http://petstore.swagger.io/v2/pet/findByStatus?status=" + str(status))
    tree = etree.XML(answer.content)
    Pets = tree.xpath('.//Pet/' + tag)
    for pet in Pets:
         print(tag + ' = ', [pet.text])
