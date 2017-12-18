import requests
# --------------------------------------------------------------------------------- #
# pet_id = 0

# pet_category_id = 0
# pet_category_name = ""

# pet_name = ""

# pet_photo_url = ""

# pet_tag_id = 0
# pet_tag_name = ""

# PET_STATUS_AVAILABLE = "available"
# PET_STATUS_PENDING = "pending"
# PET_STATUS_SOLD = "sold"
# --------------------------------------------------------------------------------- #


def get_post_pet_template(pet_id="0", pet_category_id="0", pet_category_name="string",
                          pet_name="doggie", pet_photo_url="string", pet_tag_id="0",
                          pet_tag_name="string", pet_status="available"):
    post_pet_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <Pet>
        <id>''' + pet_id + '''</id>
        <Category>
            <id>''' + pet_category_id + '''</id>
            <name>''' + pet_category_name + '''</name>
        </Category>
        <name>''' + pet_name + '''</name>
            <photoUrl>
            <photoUrl>''' + pet_photo_url + '''</photoUrl>
        </photoUrl>
        <tag>
            <Tag>
                <id>''' + pet_tag_id + '''</id>
                <name>''' + pet_tag_name + '''</name>
            </Tag>
        </tag>
        <status>''' + pet_status + '''</status>
    </Pet>'''

    return post_pet_xml



url = 'http://petstore.swagger.io/v2/pet'
header = {'accept': 'application/xml', 'Content-Type': 'application/xml'}

r = requests.post(url, data=get_post_pet_template(), headers=header)

print(r.status_code)
