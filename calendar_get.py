from bs4 import BeautifulSoup
from six.moves import urllib

# set URL to webpage with calendar
url = 'URL'

# open webpage and convert to text
htmlreq = urllib.request.urlopen(url)
html = htmlreq.read()
soup = BeautifulSoup(html, features='lxml')
text = soup.get_text()

# save to an ics file, change CAL to name of calendar
file = open('CAL.ics', 'w')
file.write(text)
file.close()
