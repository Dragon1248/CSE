import random
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

Word_bank = ["Phones', 'Tablets', 'Computer', 'Xbox One', 'Ps4', 'Memes', 'Ps3', 'Fortnite', 'Pubg', 'Rules of survival'"]
length = len(Word_bank)
range(11)
range(len(Word_bank))

randomWords = random.choice(Word_bank)

letters_guessed = []
user_input = ""

print("You have 10 guesses to win")
while user_input != "quit":
    output = []
    for letter in randomWords:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)



    if output == list(randomWords):
        print("You win")

    user_input = input("Type in a letter: ")
    letters_guessed.append(user_input)
    print(letters_guessed)

    if user_input not in list(randomWords):
        print("Guess again")