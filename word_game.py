import random

# CREATE LIST

word_list = ['jupiter', 'chemistry', 'laboratory', 'avocado', 'papaya', 'enchiladas', 'soccer', 'baseball', 'blizzard', 'tropical']

# MODULAR FUNCTIONS

def instructions():
    input("""Welcome, a random word will be selected for you to guess.
    You will get seven letter guesses. If you run out of guesses, you lose. Good luck!!
    Press 'enter' to continue.""" )
    

def pick_random():
    random_word = random.choice(word_list)
    return random_word

def hide_random(word):
    hidden_word = ''
    for i in word:
        hidden_word += ' _'
    return hidden_word

# def show_letter(word, letter):
     
# START GAME

def guessing_game():
    current_word = pick_random()
    print(current_word)
    hidden_word = hide_random(current_word)
    tries = 7
    active = True
    while active:
        instructions()
        play = input("Type 'start' to begin or 'quit' to exit. ").lower()
        if play == 'start':
            guessing = True
            correctly_guessed = ''
            while guessing:
                if tries > 0:
                    print(f'This is your hidden random word: {hidden_word}')           
                    guess = input('enter a letter. ')
                    if guess in current_word:
                         print(f'{guess} is in hidden word.')
                         correctly_guessed += guess
                         print(correctly_guessed)
                         if correctly_guessed == hidden_word:
                            print('You won the game!!')
                            return
                         else:
                            continue
                        # show_letter(current_word, guess)
                    elif guess not in current_word:
                        print(f'{guess} is not in the word, try again.')
                        tries -= 1
                else: 
                    print('Sorry, you are out of luck!! GAME OVER')
                    return
        elif play == 'quit':
            print('See ya!')
            break



guessing_game()

