import random

""" 
this a guide on how to
make hangman
1. Make a word bank - 10 items
2. Select a random item to guess
3. Take in a letter and add it to a list of letters_guessed
4. Hide and reveal letters
5. Create the win Condition
"""

word_bank = ['Phones', 'Tablets', 'Computer', 'Xbox One', 'Ps4', 'Memes', 'Ps3', 'Fortnite', 'Pubg', 'Rules of survival']


the_word = random.choice(word_bank)
print(the_word)

user_input = input("type in a letter :")
length = len(word_bank)
range(11)
range(len(word_bank))
wordsguessed = []
print(wordsguessed)

while user_input != "start":
    user_input = "type in a letter"