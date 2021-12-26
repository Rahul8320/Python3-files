import pywhatkit as kit


#kit.text_to_handwriting("Hello \nI am Rahul..\nkit.text_to_handwriting(string,save_to='location',rgb=(color code))",save_to="pic.png",rgb=(0,0,255))

#na = input("Enter your name : ")
#print("Hello "+na)
#text = input("Enter text to write : ")
#name = input("Enter photo name to save : ")
#name = name+".jpg"
#text = "\t \t"+na+"\n"+text


text = "methodology at all. The Project Management Institute (PMI)\nis anot-for-profit membership association, project management\ncertification and standards organization. They publish guidelines,\nrules and characteristics for project management, along with\nprogram and portfolio management.\nFor off, PMBOK is an acronym for Project Management Body\nof Knowledge. It’s a book, published by PMI, that collects the\nprocesses, best practices, terminologies and guidelines that are\nthe accepted norm in the industry. It was first published in 1996\nand is about to publish its sixth edition in the fall of 2017.\nThe text breaks down a project into five process groups:\ninitiating, planning, executing, controlling and closing."

# text ="So, is it a methodology or an agreed upon structure for projects? "


name = "3rd.jpg"

try:
	kit.text_to_handwriting(string=text,save_to=name,rgb=(0,0,255))
	print("Photo is saved as "+ name)

except Exception as e:
	print(e)
	
print("Thank You")
