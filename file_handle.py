import os
file = 'one.txt'
f = open(file, 'x')
f = open(file,'a')
content = input("Enter content: ")
f.write("Hello !! \nWelcome to Python.")
f.write('\n')
f.write("content is : ")
f.write('\n')
f.write(content)

f = open(file,'r')
print(f.read()) # print everything in file 

f = open(file,'r')
print(f.read(5)) # print first 5 characters

f = open(file,'r')
print(f.readline()) # print first line
print(f.readline()) # print second line

f = open(file,'r')
for x in f:
    print(x) # print line by line 

f.close()
os.remove(file)
print("Delete successfully")
