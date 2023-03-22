print("Hello, welcome to the game of hangman.")
score = 0
right_answers = ["p", "o", "s", "n", "y"]
wrong_answers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "q", "r", "t", "u", "v", "w", "x", "z"]
max_wrong_answers = 6
max_right_answers = 6


while True:

	answer = input("Whats your letter? ")

	if answer in right_answers:
		print("correct")
		score += 1
		if score == max_right_answers:
			print("You Win you have got all", + max_right_answers, "correct")
			break

	elif answer in wrong_answers:
		print("Wrong")
		score += 1
		if score >= max_wrong_answers:
			print("So sorry, you've reached", + max_wrong_answers, "wrong answers.")
			break
	else:
		print("Please enter an answer!")
