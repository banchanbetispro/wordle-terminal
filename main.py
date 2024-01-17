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
    while not win:
        randomWord = random.choice(data).split()
        wordsArray = randomWord + [''] * random.randint(3,9)
        tries = 1
        userPrompt = input("Choose a word: ")
        for char in userPrompt:
            if char not in randomWord:
                wordsArray[tries] += (COLORS[0] + char)
            elif userPrompt.index(char) != randomWord.index(char):
                wordsArray[tries] += (COLORS[1] + char)
            else:
                wordsArray[tries] += (COLORS[2] + char)
                win = True
        if wordsArray[-1]:
            break
        for i in range(1,len(wordsArray)):
            print(wordsArray[i])
    print("You won!" if win else "You lost :(")

if __name__ == "__main__":
    main()
