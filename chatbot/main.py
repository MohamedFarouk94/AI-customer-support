from ask import ask_and_answer


if __name__ == '__main__':
	print("\nASSISTANT: Hi! I'm here to help you in anything related to our products and policy. How can I help you?")
	while True:
		print()
		question = input("YOU: ")
		if question == "exit":
			break
		answer = ask_and_answer(question)
		print(f"\nASSISTANT: {answer}")

	print("Goodbye!")
