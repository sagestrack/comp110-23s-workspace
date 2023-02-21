"""Wordle Exercise"""
__author__ = "730331072"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""

def contains_char(guess: str, char: str) -> bool:
    """checks if a character is contained in the user's guess"""
    assert len(char) == 1
    char_idx: int = 0
    while char_idx < len(guess):
        if guess[char_idx] == char:
            return True
        else:
            char_idx = char_idx + 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """returns emoji representing letter status"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    guess_idx: int = 0
    assert len(guess) == len(secret_word)
    while guess_idx < len(secret_word):
        if guess[guess_idx] == secret_word[guess_idx]:
            emoji += GREEN_BOX
        elif contains_char(secret_word, guess[guess_idx]) == True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        guess_idx = guess_idx + 1
    return emoji

def input_guess(input_guess: int) -> str:
    """prompts user for guess of the correct length"""
    guess: str = input(f"Enter a {input_guess}-character word: ")
    while len(guess) != input_guess:
        guess = input(f"That was not {str(input_guess)} letters! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "python"
    turn: int = 1
    while turn <=6 :
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            return print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()