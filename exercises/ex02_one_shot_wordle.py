"""One Shot Wordle."""

__author__: str = "730466575"


wordle: str = "pick"
word: str = input("What is your " + str(len(wordle)) + "-letter guess? ")
emojis: str = ""
letter_check: bool = False
index: int = 0

while len(word) != len(wordle):
    word = input("That was not 6 letters! Try again: ")

while index < len(wordle):
    if word[index] == wordle[index]:
        emojis += "\U0001F7E9"
    else:
        i: int = 0
        while i < len(wordle):
            if wordle[i] == word[index]:
                letter_check = True
                i = len(wordle)
            else:
                i += 1
        if letter_check:
            emojis += "\U0001F7E8"
        else:
            emojis += "\U00002B1C"
    letter_check = False
    
    index += 1


if word != wordle:
    print(emojis)
    print("Note quite. Play again soon!")
else:
    print(emojis)
    print("Woo! You got it!")
