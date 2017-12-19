from api_functional.pet.pet import *


def test_tags():
    tags = PetGetTags(1111)
    assert tags.get_id_tag() == "1111"
