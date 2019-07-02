# -*- coding: utf-8 -*-
# @Author: Nitesh
# @Date:   2017-04-05 23:50:19
# @Last Modified by:   Nitesh
# @Last Modified time: 2019-07-02 16:04:25

from string import ascii_lowercase
from words import choose_word

def get_number_attempts():
	#Get user input for number of incorrect attempt
	while True:
		num_attempts= input("Enter the number of incorrect attempts you want.[1-25]:")
		try:
			num_attempts=int(num_attempts)
			if 1<= num_attempts <=25:
				return num_attempts
			else:
				print('{} is not between 1 and 25'.format(num_attempts))
		except ValueError:
			print('{} is not an integer between 1 and 25'.format(num_attempts))

def get_word_length():
	#Get user input ofr word length.
	while True:
		word_length=input("Enter the maximum word length you want to guess.[4-16]:")

		try:
			word_length=int(word_length)
			if 4<= word_length <=16:
				return word_length
			else:
				print('{} is not between 4 and 16'.format(word_length))
		except ValueError:
			print('{} is not an integer between 4 and 16'.format(word_length))

def get_display_word(word,check):
	#Get the word
	if len(word) !=len(check):
		raise ValueError("Word length and indices length are not same")
	display_word=''.join([letter if check[i] else '*' for i, letter in enumerate(word)])
	return display_word.strip()

def get_next_letter(remaining_letters):
	#Get user input
	if len(remaining_letters)==0:
		raise ValueError("There is no remianing letters")
	while True:
		next_letter=input("Guess the next letter:").lower()
		if len(next_letter) !=1:
			print("{} is not a single character".format(next_letter))
		elif next_letter not in ascii_lowercase:
			print("{} is not a letter".format(next_letter))
		elif next_letter not in remaining_letters:
			print("{} has been guessed before".format(next_letter))
		else:
			remaining_letters.remove(next_letter)
			return next_letter
def play_hangman():
	#Play a game of hangman 
	print('Starting a game of Hangman...')
	attempts_remaining=get_number_attempts()
	#print(attempts_remaining)
	word_length=get_word_length()
	#Randomly select a word
	print('Selecting a word...')
	word=choose_word(word_length)
	print()
	check=[letter not in ascii_lowercase for letter in word]
	remaining_letters=set(ascii_lowercase)
	#print(remaining_letters)
	wrong_letters=[]
	word_solved=False
	#Main game loop
	while attempts_remaining>0 and not word_solved:
		#print current game state
		print("Word:{}".format(get_display_word(word,check)))
		print("Attempts Remaining:{}".format(attempts_remaining))
		print("Previous Guesses:{}".format(" ".join(wrong_letters)))

		#Get player's next letter guess
		next_letter =get_next_letter(remaining_letters)

		#check if letter guess is in word
		if next_letter in word:
			#Guessed correctly
			print("{} is in the word!".format(next_letter))

			#Reveal matching letters
			for i in range(len(word)):
				if word[i] ==next_letter:
					check[i]=True
		else:
			#Guessed incorrectly
			print("{} is not in the word!".format(next_letter))

			#Decrement number of attempts left and append guess to wrong guesses
			attempts_remaining-=1
			wrong_letters.append(next_letter)
			#Check if word is completely solved
		if False not in check:
			word_solved =True
		print()

	#The game is over: reveal the word
	print("The word is {}".format(word))

	#Notify player of victory or defeat
	if word_solved:
		print("Congratulations! You won!")
	else:
		print("Try again next time!")

	#Ask player if he/she wants to try again
	try_again=input("Would you like play again?[y/Y]")
	return try_again.lower()=='y'

if __name__=='__main__':
	while play_hangman():
		print()

