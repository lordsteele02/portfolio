 
import random
import words
import hangmanimages


lives = 6
already_guessed = []


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
game_over = False
print(hangmanimages.logo)

display = []

for blank in chosen_word:
    display += ["_"]
print (display)


while game_over == False:
    
    guess = input("Guess a letter: ").lower()
    

    for _ in range(word_length):
        if chosen_word[_] == guess:
            display[_] = guess
    print(display)

    if guess in display and guess in already_guessed:
        print(f"you already guessed '{guess}', try again.")

    if "_" not in display:
        print("You win")
        game_over = True
    
    
    if guess not in display and guess in already_guessed:
        print(f"you already guessed '{guess}', try again.")
    elif guess not in display and guess not in already_guessed:
        print(hangmanimages.stages[lives])
        lives -= 1
        if lives < 0:
            game_over = True
            print("You Lose!")
            print(f"The answer is: {chosen_word}")
    already_guessed += guess
    
    
