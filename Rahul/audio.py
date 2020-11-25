from playsound import playsound
import os
import random

path = r'\C:\Users\Windows 10\Desktop\Web-Py\audio'
files = os.listdir(path)
d = random.choice()
playsound(d)
