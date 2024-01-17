from api import data
import random
import pyfiglet
from colorama import Fore

COLORS = [Fore.RED,Fore.YELLOW,Fore.GREEN]

def greet():
    print(pyfiglet.figlet_format("Wordle"))

def main():
    greet()
    win = False
    randomWord = random.choice(data)
    wordsArray = []
    tries = 1
    #print(wordsArray)
    print("The secret word has", len(randomWord), "letters")
    while not win and tries < 7:
        userPrompt = input("Choose a word: ")
        #print(len(userPrompt),len(randomWord),randomWord)
        if len(userPrompt) != len(randomWord):
            print("Invalid input")
        else:
            if userPrompt == randomWord:
                win = True
            else:
                array = []
                if userPrompt == randomWord:
                    array.append(COLORS[2] + userPrompt)
                    break
                for charIndex in range(len(userPrompt)):
                    if userPrompt[charIndex] not in randomWord:
                        array.append(COLORS[0] + userPrompt[charIndex])
                    elif userPrompt[charIndex] != randomWord[charIndex]:
                        array.append(COLORS[1] + userPrompt[charIndex])
                    else:
                        array.append(COLORS[2] + userPrompt[charIndex])
                #print(array)
                wordsArray.append("".join(array))
                tries += 1
        if win == True:
            break
        for i in wordsArray[1:]:
            print(i)
            print("-"*len(randomWord))
    print("You won!" if win else f"You lost :(, the given word was {randomWord}")

if __name__ == "__main__":
    main()
