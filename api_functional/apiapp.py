import requests
from lxml import etree

from api_functional.pet.pet_creator import Creator
from api_functional.pet.pet_functional import PetDriver

petnew = Creator()

pdriver = PetDriver()
newid = petnew.createPet(name='Andrii', status='IDoThis')
print(newid)
print(pdriver.update_by_id(newid, "312 team", "we do this"))
