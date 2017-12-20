from api_functional.pet_func.pet import *


def test_tags():
    tags = PetGetTags(1111)
    assert tags.get_id_tag() == "1111"
