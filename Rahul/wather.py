
import requests
from bs4 import BeautifulSoup

city = input("Enter your city: ")
search = "weather in " + str(city)

url = f"https://www.google.com/search?&q={search}"

r = requests.get(url)

s = BeautifulSoup(r.text, "html.parser")

update = s.find("div", class_="BNeawe").text

print(city +"  :  "+ update)
