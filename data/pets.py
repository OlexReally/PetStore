from data.pet_provider import PetProvider

'''
        self.__pet_id = pet_id                      # int
        self.__pet_category_id = pet_category_id    # int
        self.__pet_category_name = pet_category_name
        self.__pet_name = pet_name
        self.__pet_photo_url = pet_photo_url
        self.__pet_tag_id = pet_tag_id              # int
        self.__pet_tag_name = pet_tag_name
        self.__pet_status = pet_status
'''

# available
# pending
# sold


def get_rabbit():
    return PetProvider(pet_id="1111",
                       pet_category_id="345",
                       pet_category_name="home",
                       pet_name="rabbit",
                       pet_photo_url="string",
                       pet_tag_id="543",
                       pet_tag_name="tag",
                       pet_status="available")

