"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730466575"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters.")

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")

print("Searching for " + letter + " in " + word + ".")

tally: int = 0

if letter == word[0]:
    tally += 1
    print(letter + " found at index 0")

if letter == word[1]:
    tally += 1
    print(letter + " found at index 1")

if letter == word[2]:
    tally += 1
    print(letter + " found at index 2")

if letter == word[3]:
    tally += 1
    print(letter + " found at index 3")

if letter == word[4]:
    tally += 1
    print(letter + " found at index 4")

if tally > 0:
    print(str(tally) + " instances of " + letter + " found in " + word + ".")
else:
    print("No instances of " + letter + " found in " + word + ".")
