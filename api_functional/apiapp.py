import requests
from lxml import objectify
from lxml import etree

url = "http://petstore.swagger.io/v2/pet/findByStatus?status=available"
headers = {'accept': 'application/xml'}
r = requests.get(url, headers=headers)

print(r.content)
tree = etree.XML(r.content)
Pets = tree.xpath('.//Pet/name') # дістаємо ліст всіх петів
for pet in Pets: # перебираємо петнейми
    print('text =', [pet.text]) # виводимо петів

url = "http://petstore.swagger.io/v2/pet/5678"
headers = {'accept': 'application/xml'}
p = requests.get(url, headers=headers)
#pet = etree.XML(p.content)
o = objectify.fromstring(p.content)
print(o.name.text)

