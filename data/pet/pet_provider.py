class PetProvider:
    def __init__(self, pet_id="0", pet_category_id="0", pet_category_name="string",
                 pet_name="doggie", pet_photo_url="string", pet_tag_id="0",
                 pet_tag_name="string", pet_status="available"):
        self.__pet_id = pet_id
        self.__pet_category_id = pet_category_id
        self.__pet_category_name = pet_category_name
        self.__pet_name = pet_name
        self.__pet_photo_url = pet_photo_url
        self.__pet_tag_id = pet_tag_id
        self.__pet_tag_name = pet_tag_name
        self.__pet_status = pet_status

    @property
    def id(self):
        return self.__pet_id

    @property
    def category_id(self):
        return self.__pet_category_id

    @property
    def category_name(self):
        return self.__pet_category_name

    @property
    def name(self):
        return self.__pet_name

    @property
    def photo_url(self):
        return self.__pet_photo_url

    @property
    def tag_id(self):
        return self.__pet_tag_id

    @property
    def tag_name(self):
        return self.__pet_tag_name

    @property
    def status(self):
        return self.__pet_status

    # -------------------------------------------------------------------------------------------

    def post_pet_xml(self):
        post_pet_xml = '''<?xml version="1.0" encoding="UTF-8"?>
        <Pet>
            <id>''' + self.pet_id + '''</id>
            <Category>
                <id>''' + self.pet_category_id + '''</id>
                <name>''' + self.pet_category_name + '''</name>
            </Category>
            <name>''' + self.pet_name + '''</name>
                <photoUrl>
                <photoUrl>''' + self.pet_photo_url + '''</photoUrl>
            </photoUrl>
            <tag>
                <Tag>
                    <id>''' + self.pet_tag_id + '''</id>
                    <name>''' + self.pet_tag_name + '''</name>
                </Tag>
            </tag>
            <status>''' + self.pet_status + '''</status>
        </Pet>'''

        return post_pet_xml
