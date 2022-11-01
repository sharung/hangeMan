import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

display = []
lives = 6

rand_word = random.choice(word_list)
lan_word = len(rand_word)

for latter in range(lan_word):
    display += "_"

game = False
while not game:
    guess = input("Guess the latter : ").lower()

    if guess in display:
        print("You've all ready guest")

    for i in range(lan_word):
        if guess in rand_word[i]:
            display[i] = guess
    
    
    if guess not in rand_word:
        lives -= 1
        print(f"You lose you live {lives}, {guess} not the right")
        if lives == 0:
            game = True
            print("Game over")
    
    print(f"{' '.join(display)}")

    print(stages[lives])
    
    if "_" not in display:
        game = True
        print("You win!")
