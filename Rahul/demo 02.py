
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
while True:

    test = input("Enter your text.: ")
    engine.say(test)

    engine.runAndWait()
