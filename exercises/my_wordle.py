"""Structured Wordle."""

from random import randint

author = "730466575"


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
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += "\U0001F7E9"
        elif contains_char(secret, guess[i]):
            emoji += "\U0001F7E8"
        else:
            emoji += "\U00002B1C"
        i += 1

    return emoji


def input_guess(exp_len: int) -> str:
    user_input: str = input(f"Enter a {exp_len} character word: ")
    while len(user_input) != exp_len:
        user_input = input(f"That wasn't {exp_len} characters! Try again: ")
    
    return user_input


def main() -> None:
    """The entrypoint of the porgram and main game loop."""
    turn: int = 1
    words: list[str] = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief", "Child", "China", "Claim", "Class", "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft", "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry", "Error", "Event", "Faith", "Fault", "Field", "Fight", "Final", "Floor", "Focus", "Force", "Frame", "Frank", "Front", "Fruit", "Glass", "Grant", "Grass", "Green", "Group", "Guide", "Heart", "Henry", "Horse", "Hotel", "House", "Image", "Index", "Input", "Issue", "Japan", "Jones", "Judge", "Knife", "Laura", "Layer", "Level", "Lewis", "Light", "Limit", "Lunch", "Major", "March", "Match", "Metal", "Model", "Money", "Month", "Motor", "Mouth", "Music", "Night", "Noise", "North", "Novel", "Nurse", "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party", "Peace", "Peter", "Phase", "Phone", "Piece", "Pilot", "Pitch", "Place", "Plane", "Plant", "Plate", "Point", "Pound", "Power", "Press", "Price", "Pride", "Prize", "Proof", "Queen", "Radio", "Range", "Ratio", "Reply", "Right", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Scope", "Score", "Sense", "Shape", "Share", "Sheep", "Sheet", "Shift", "Shirt", "Shock", "Sight", "Simon", "Skill", "Sleep", "Smile", "Smith", "Smoke", "Sound", "South", "Space", "Speed", "Spite", "Sport", "Squad", "Staff", "Stage", "Start", "State", "Steam", "Steel", "Stock", "Stone", "Store", "Study", "Stuff", "Style", "Sugar", "Table", "Taste", "Terry", "Theme", "Thing", "Title", "Total", "Touch", "Tower", "Track", "Trade", "Train", "Trend", "Trial", "Trust", "Truth", "Uncle", "Union", "Unity", "Value", "Video", "Visit", "Voice", "Waste", "Watch", "Water", "While", "White", "Whole", "Woman", "World", "Youth"]
    secret: str = words[randint(0, len(words))]
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret.lower():
            print(f"You won in {turn}/6 turns!")
            turn = 7
        else:
            turn += 1
            if turn > 6:
                print("X/6 - Sorry, try again tomorrow!")
                print(secret)
                quit()


if __name__ == "__main__":
    main()