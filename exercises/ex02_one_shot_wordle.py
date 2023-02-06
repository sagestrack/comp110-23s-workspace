"""One-Shot Wordle Exercise"""
__author__ = "730331072"

secret_word: str = "python"
guess: str = input(f"What is your {str(len(secret_word))}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_idx: int = 0
secret_word_idx: int = 0
emoji: str = ""
chr_contain: bool = False
alt_idx: int = 0

if len(guess) != len(secret_word):
    guess: str = input(f"That was not {str(len(secret_word))} letters! Try again: ")
if len(guess) == len(secret_word):
    while guess_idx < len(secret_word):
        if guess[guess_idx] == secret_word[guess_idx]:
            emoji = emoji + GREEN_BOX
        else:
            while chr_contain == False and guess_idx < len(secret_word) and alt_idx < len(secret_word):
                if guess[guess_idx] == secret_word[alt_idx]:
                    chr_contain = True
                else:
                    alt_idx = alt_idx + 1
            if chr_contain == True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        guess_idx = guess_idx + 1
    print(emoji)
    if guess != secret_word:
        print ("Not quite. Play again soon!")
    else:
        print ("Woo! You got it!")

