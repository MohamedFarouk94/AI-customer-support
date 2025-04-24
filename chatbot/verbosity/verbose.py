def print_json(data):
	if data['irrelevant']:
		print("[thinking] The question sounds irrelevant.")
		return

	print(f"[thinking] Enhanced version of the question: {data['rewritten-question']}")

	if data['products-keywords']:
		print(f"[thinking] Keywords for related products docs: {data['products-keywords']}")
	else:
		print(f"[thinking] The question does not need products data.")

	if data['policy-keywords']:
		print(f"[thinking] Keywords for related policy docs: {data['policy-keywords']}")
	else:
		print(f"[thinking] The question does not need policy data.")


def print_helping_lines():
	print("\n[help] Type 'exit' without quotations to end the conversation.")
	print("[help] Type 'exit-save' without quotations to end the conversation.\n")
