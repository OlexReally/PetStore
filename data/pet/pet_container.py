from data.pet.pet_provider import PetProvider


def pet_rabbit():
    return PetProvider(pet_id="1112",
                       pet_category_id="345",
                       pet_category_name="home",
                       pet_name="rabbit",
                       pet_photo_url="string",
                       pet_tag_id="543",
                       pet_tag_name="tag",
                       pet_status="available")


def pet_dog():
    return PetProvider(pet_id="1113",
                       pet_category_id="346",
                       pet_category_name="yard",
                       pet_name="dog",
                       pet_photo_url="string",
                       pet_tag_id="544",
                       pet_tag_name="tag",
                       pet_status="available")


def pet_cat():
    return PetProvider(pet_id="1114",
                       pet_category_id="347",
                       pet_category_name="home",
                       pet_name="rabbit",
                       pet_photo_url="string",
                       pet_tag_id="545",
                       pet_tag_name="tag",
                       pet_status="available")
