"""Structured Wordle."""

__author__: str = "730466575"


def contains_char(word: str, letter: str) -> bool:
    """Search for character in word."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word):
        if letter == word[i]:
            return True
        i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns the emoji associated with the letter."""
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += "\U0001F7E9"
        elif contains_char(secret, guess[i]):
            emoji += "\U0001F7E8"
        elif not contains_char(secret, guess[i]):
            emoji += "\U00002B1C"
        i += 1

    return emoji


def input_guess(length: int) -> str:
    """Makes sure user guess equals the length of the secret word."""
    user_input: str = input(f"Enter a {length} character word: ")
    while len(user_input) != length:
        user_input = input(f"That wasn't {length} chars! Try again: ")
    
    return user_input


def main() -> None:
    """The entrypoint of the porgram and main game loop."""
    turn: int = 1
    secret: str = "codes"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 7
        else:
            turn += 1
        
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")
                

if __name__ == "__main__":
    main()