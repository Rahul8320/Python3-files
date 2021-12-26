import pywhatkit as kit

#kit.search("pywhatkit python")

text = input("Enter your query : ")
try:
	kit.info(topic=text)
except Exception as e:
	print(e)
	
