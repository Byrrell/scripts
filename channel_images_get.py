import requests
import shutil
from bs4 import BeautifulSoup

def download_image(url, file_name):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)

with open(r'channels.xml', 'r') as f:
    data = f.read()

import xml.etree.ElementTree as ET

tree = ET.parse(r'channels.xml')

root = tree.getroot()

for i in range(len(root)):
    url = str(root[i][2].attrib['src'])
    file_name = str(root[i][0].text + '.png')

    download_image(url, file_name)
