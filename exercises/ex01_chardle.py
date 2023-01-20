""""Chardle Exercise"""
__author__= "730331072"

word: str = input("Enter a 5-character word: ")
if len(word)!=5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if len(character)!=1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + character + " in " + word)

if (word[0] == character):
    print(character + " found at index 0")
if (word[1] == character):
    print(character + " found at index 1")
if (word[2] == character):
    print(character + " found at index 2")
if (word[3] == character):
    print(character + " found at index 3")
if (word[4] == character):
    print(character + " found at index 4")
    
"""Stuck on part 3"""
count: str = 0
if sum(True>=1):
    count == count + 1
    print(count + "instance of "+character+ " found in "+ word)

