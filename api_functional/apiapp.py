from api_functional.pet.pet_functional import *

petd = PetDriver('http://petstore.swagger.io/')
status = Status
id = petd.create_pet(name='Andrii', status=status.AVAILABLE)
print(id)

petd.update(id, name='Sanja', status=status.PENDING)
print(petd.get_xml(id))

petd.update(id, name='Andrii')
print(petd.get_xml(id))

petd.update(id, status=status.AVAILABLE)
print(petd.get_xml(id))
