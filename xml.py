import xml.etree.ElementTree as ET
import requests

xml_response=requests.get("https://forecast.weather.gov/MapClick.php?lat=25.9879&lon=-97.5555&FcstType=digitalDWML")

root = ET.fromstring(xml_response.content)

for child in root.iter('value'):
    print(child.tag,child.text)
