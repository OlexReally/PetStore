from lxml import objectify
from api_functional.Request import getapi


class PetGetTags:
    def __init__(self, pet_id):
        self.r = getapi("http://petstore.swagger.io/v2/pet/" + str(pet_id))
        self.o = objectify.fromstring(self.r.content)

    def get_id_tag(self):
        return self.o.id.text

    def get_name_tag(self):
        return self.o.name.text

    def get_photourls_tag(self):
        return self.o.photoUrls.text

    def get_status_tag(self):
        return self.o.status.text

    def get_tags_tag(self):
        return self.o.tags.text
