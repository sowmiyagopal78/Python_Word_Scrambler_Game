import random

# Predefined list of words for the game
words = ['sofa', 'apple', 'mixer', 'stove', 'book', 'fridge']

# Prompt user to play or skip
choice = input('Would you like to Guess ? Skip ? ').strip().lower()

if choice == 'skip':
    print('Thanks for participating')
else:
    # Pick a random word and scramble its letters
    random_word = random.choice(words).lower()
    letters = list(random_word)
    random.shuffle(letters)
    scrambled_word = ''.join(letters).upper()

    print(f'This is your scrambled word: {scrambled_word}')

    # Get user guess and evaluate
    user_guess = input('Enter your guess: ').strip().lower()
    if user_guess == random_word:
        print('Wohoo! Great, Spot On')
    else:
        print(f'Hmm, Sorry the correct word was: {random_word.upper()}')