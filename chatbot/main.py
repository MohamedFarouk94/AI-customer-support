from ask import ask_and_answer
from memory.history import update_full_history, save_history
from verbosity.verbose import print_helping_lines


first_message = "Hi! I'm here to help you in anything related to our products and policy. How can I help you?"


if __name__ == '__main__':
	print(f"\nASSISTANT: {first_message}")
	print_helping_lines()
	update_full_history("ASSISTANT", first_message)

	while True:
		print()
		question = input("YOU: ")

		if question == "exit":
			break

		if question == 'exit-save':
			save_history()
			break

		answer = ask_and_answer(question)
		print(f"\nASSISTANT: {answer}")
		print_helping_lines()

	print("Goodbye!")
