"""
    [+] Created on Thu May 13 12:23:19 2021
    [+] Project on Python3
    [*] By Rahul Dey
    [+] @author: mine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as re
from bs4 import BeautifulSoup as bs
import pandas as pd


wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link = re.get(wiki_link).text

soup = bs(link,'lxml')
print(soup.title)

#all_link = soup.find_all("a")

right_table = soup.find('table',class_="wikitable sortable")

table_links = right_table.findAll('a')
country = []
for link in table_links:
    country.append(link.get('title'))

i = 1
for k in country:
    print(i," ---> ",k)
    i+=1

df = pd.DataFrame()
df['country'] = country
#print(df)
