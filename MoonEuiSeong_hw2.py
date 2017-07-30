import pymysql
import requests
import urllib
import zipfile
import sys
import glob, os
from bs4 import BeautifulSoup
url="http://fl0ckfl0ck.info";	



soup=BeautifulSoup(urllib.request.urlopen(url).read(),"lxml")

print("Entire web source")
print(soup)

print("A fragment of web source you can see href data")
u=0
for link in soup.find_all('a'):
        print(link.get('href'))

    
