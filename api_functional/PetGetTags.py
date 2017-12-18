from lxml import objectify


class PetGetTags:
    def __init__(self, request):
        self.o = objectify.fromstring(request.content)

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
