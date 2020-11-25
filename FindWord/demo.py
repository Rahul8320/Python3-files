
lines =[]
file = open("abc2.txt", 'r')

for line in file:
    line.replace("\n", " ")
    line = line.split(" ")
    for word in line:
        word.replace("\n", "")
        lines.append(word)

    # print(line)

file.close()
print(lines)