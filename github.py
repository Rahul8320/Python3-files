"""
    [+] Created on Mon May 24 09:52:50 2021
    [+] Project on Python3
    [*] By Rahul Dey
    [+] @author: mine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

github_user = input(" Enter Github username >>> ")
url = "https://github.com/" + github_user

r = requests.get(url)
soup = bs(r.content,'html.parser')
profile_image = soup.find('img',{'alt':'Avatar'})['src']
print(profile_image)

