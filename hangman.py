
import random
import string
from hangman_words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def print_update(word, used_letters, lives):

    #   draw hangman
    draw_hangman(lives)
    print(f'\u2764\uFE0F  : {lives}')
    #   used letters
    print('You have used these letters: ', ', '.join(used_letters))
        
    #   Current word
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))


def draw_hangman(lives):
    if lives == 6:
        print("________ ")
        print("| | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif lives == 5:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| ")
        print("| ")
        print("| ")
    elif lives == 4:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif lives == 3:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif lives == 2:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\\ ")
        print("| ")
        print("| ")
    elif lives == 1:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\\ ")
        print("| / ")
        print("| ")
    elif lives == 0:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\\ ")
        print("| / \\ ")
        print("| ")


def hangman():
    # set-up
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    #print(word)


    while len(word_letters) > 0 and lives > 0:

        # Update
        print_update(word, used_letters, lives)

        # Getting player input
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)    
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('wrong')
        elif user_letter in used_letters:
            print('You have already used that letter')
        else: 
            print('Invalid character!!!')


        print('\n')

    
    if lives > 0:
        draw_hangman(lives)
        print('You Won!')
    
    else:
        draw_hangman(lives)
        print(f'Sorry! You Lost, the word was: {word}')
        


hangman()



