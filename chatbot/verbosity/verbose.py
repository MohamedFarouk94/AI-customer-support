verbosity = True


def get_verbose_flag():
	global verbosity
	return verbosity


def flip_verbose_flag():
	global verbosity
	verbosity = not verbosity


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
