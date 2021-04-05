from string import ascii_lowercase
from random import randint

attempts = 7
remaining_letters = list(ascii_lowercase)


def print_field(field):
	print(' '.join(field))


def make_guess():
	while True:
		guess = input('Please enter your guess: ')

		if len(guess) != 1:
			print('You must guess a single letter.')
		elif guess.isnumeric():
			print('That is not a letter.')
		else:
			if guess not in remaining_letters:
				print('You have already guessed that letter.')
			else:
				remaining_letters.remove(guess)
				return guess

player_two = input('Please enter the name of the player that provides the word: ')
word = (input('Please enter your word: ')).lower()

print('\n' * 30)

player_one = input('Please enter the name of the guessing player: ')

print('\n' * 30)

field = ['_' for letter in list(word)]

while attempts > 0 and '_' in field:
	print_field(field)
	print('Unguessed letters:', ' '.join(remaining_letters))
	print('Remaining attempts:', attempts)
	turn = make_guess()

	if turn in list(word):
		positions = [i for i, letter in enumerate(list(word)) if letter == turn]

		for position in positions:
			field[position] = turn
	else:
		print(turn, 'is not in the word.')
		attempts -= 1


print_field(field)

if '_' not in field:
	print(f'Congratulations! {player_one} has won.')
else:
	print(f'Congratulations! {player_two} has won.')