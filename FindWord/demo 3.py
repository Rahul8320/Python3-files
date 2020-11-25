# count number of line in text file .

file = open("abc2.txt", "r")
count = 0

text = file.read()
text = text.replace("?", ".").replace("!", ".")
line = text.split(".")

for i in line:
    if i:
        count += 1

print(f"Total number of lines : {count}")