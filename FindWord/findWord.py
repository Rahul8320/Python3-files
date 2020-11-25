
import os
ENDC = '\033[m'
TGREEN = '\033[32m'
SCOL = '\033[31m'
FCOL = '\033[35m'
NCOL = '\033[34m'
COL = '\033[36m'

dir_contents = os.listdir()
print(NCOL + " Your directory contents:  ")
print(dir_contents, ENDC)

word = input("Enter the word u want to search :  ")
word = word.lower()


def isword(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
        # print(filecontent)
        if word in filecontent.lower():
            f.close()
            return True
        else:
            f.close()
            return False


def countword(file):
    count = 0
    with open(file, 'r') as f:
        line = f.read().splitlines()
        text = " ".join(line)
        text = text.split(" ")

    for w in text:
        w = w.lower().replace(".", "").replace(",", "").replace(")", "").replace("(", "").replace("/", "")
        w = w.replace("?", "").replace("!", "")
        if w == word:
            count += 1

    f.close()
    return count


if __name__ == "__main__":
    for item in dir_contents:
        if item.endswith('txt'):
            print(TGREEN + f"searching {word} for {item} .......", ENDC)
            flag = isword(item)
            if flag:
                print(SCOL + f" *{word}* is DETECT in {item}.", ENDC)
                key = input("Do u want to search how many time present in the file (y/N) :  ")
                if key.lower() == "y":
                    flg = countword(item)
                    print(COL + f" *{word}* is present {flg} time in {item}", ENDC)
                else:
                    pass
            else:
                print(FCOL + " XXXXXXXXXXXXXXXXXXXX", ENDC)

