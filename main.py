import country
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#chose_country = random.choice(pycountry.countries)

word_choice = (random.choice(country.country_name)).lower()

Life = 6

print(word_choice)
placeholder = ""
for i in range(len(word_choice)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_latters = []

while game_over != True:
    guess = input("Guess the letter: ").lower()         #User Guess letter 
    print(guess)

    display = ""

    for letter in word_choice:
        if letter == guess:
            display += letter
            correct_latters.append(guess)
        elif letter in correct_latters:
            display += letter
        else:
            display += "_"
    print(display) 

    if guess not in word_choice:
        Life -= 1
        if Life == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("you win")
        
    print(stages[Life])