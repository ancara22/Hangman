import random
import os
import hangman_words
import hangman_stages

from playsound import playsound

s_1 = "/Users/dinisbarcari/Desktop/100 python/done.wav"
s_2 = "/Users/dinisbarcari/Desktop/100 python/cancel.wav"
s_3 = "/Users/dinisbarcari/Desktop/100 python/yes.wav"
s_1 = s_1.replace(" ", "%20")
s_2 = s_2.replace(" ", "%20")
s_3 = s_3.replace(" ", "%20")








lives = 6
end_game = False
str_list = []
word = random.choice(hangman_words.words_list)


for i in range(0, len(word)):
	str_list += "_"
print("".join(str_list))


def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def check(letter):
	yes = False
	for x in range(0, len(word)):
		if letter == word[x]:
			str_list[x] = letter
			yes = True
	if yes:
		playsound(s_3)

def print_stage_word(liv, string):
	clear_screen()
	print(hangman_stages.stages[liv])
	print("".join(string))


def start(end, liv):
	while not end:
		letter = input("Choose letter:")
		check(letter)
		print_stage_word(liv, str_list)

		if "_" not in str_list:
			print("You Win!")
			end = True
		elif letter not in str_list:
			liv -= 1
			if liv <= 0:
				print_stage_word(liv, str_list)
				print("Game over!")

				end = True
			else:
				print_stage_word(liv, str_list)


start(end_game, lives)
