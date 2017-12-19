import requests
from lxml import etree

from api_functional.pet.pet_creator import Creator

petnew = Creator()
print(petnew.createPet(name='Andrii', status='IDoThis'))

