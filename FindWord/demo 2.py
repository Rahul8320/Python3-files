# count number of occurrence of same word in text file

count = 0

with open('abc2.txt', 'r') as f:
    line = f.read().splitlines()
    text = " ".join(line)
    text = text.split(" ")

for word in text:
    word = word.lower().replace(".", "").replace(",", "").replace(")", "").replace("(", "").replace("/", "")
    word = word.replace("?", "").replace("!", "")
    if word == "hacker":
        count += 1

f.close()
print(count)
print("Thank you")