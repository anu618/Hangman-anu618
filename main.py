import random
import string

from words import words


def get_valid_word(words_list):
    valid_word = random.choice(words_list)
    while ' ' in valid_word or ' ' in valid_word:
        valid_word = random.choice(words)

    return valid_word.upper()


word = get_valid_word(words)
word_letters = set(word)
alphabets = set(string.ascii_uppercase)
used_letters = set()

print(word)

tries = 6

while len(word_letters) > 0 and tries > 0:
    print('You have ', tries, ' tries left. You have used these letters: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current Word:', ' '.join(word_list))

    user_letter = input('Guess a letter:').upper()

    if user_letter in alphabets - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        else:
            tries = tries - 1
            print('Letter is not in the word.')

    elif user_letter in used_letters:
        print('You have already guessed that letter. Please try a different letter.')

    else:
        print('Invalid character. Please enter a valid alphabet.')

if tries == 0:
    print('You died. Better luck next time! The word was ', ' '.join(word))
else:
    print('Yay! You guessed the word, ', word, ' correctly')
