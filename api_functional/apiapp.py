import requests
from lxml import etree

from api_functional.tool.xml_tool import *

b = XML_Tool()
print(b.get_xml_from_webapi(1112))