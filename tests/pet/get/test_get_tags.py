from api_functional.PetGetTags import *


def test_tags():
    tags = PetGetTags(1111)
    assert tags.get_id_tag() == "1111"
