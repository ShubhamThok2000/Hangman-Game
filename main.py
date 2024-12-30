import country
import random
import hangman_art


#chose_country = random.choice(pycountry.countries)

word_choice = (random.choice(country.country_name)).lower()

Life = 6

print(hangman_art.logo)
#print(word_choice)
placeholder = ""
for i in range(len(word_choice)):
    placeholder += "_"

print(placeholder)

game_over = False
correct_latters = []

while game_over != True:

    print(f"***********{Life}/6 Life Left********")
    guess = input("Guess the letter: ").lower()         #User Guess letter 

    if guess in correct_latters:
        print(f"You've already guess the letter {guess}")
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
        print(f"You've guess word "{guess}" and its not in the word so you have lose the life")
        if Life == 0:
            game_over = True
            print(f"************ IT was {word_choice}! _You_Lose_*************")

    if "_" not in display:
        game_over = True
        print("*****************************_YOU_WON_***************************")

    #Pint Hang-man Piture    
    print(hangman_art.stages[Life])