from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
article = urlopen(url, context=ctx).read()
parsed_article = BeautifulSoup(article, "lxml")

text_chunks = parsed_article.find_all('p') # Returns a list of paragraphs
text = "" # Declaring a string

for chunk in text_chunks:
    text += chunk.text #.text converts each paragraph into a text that we can read

#print (text)
