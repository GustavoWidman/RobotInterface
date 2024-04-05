import re

colors = {
	'0': '\x1b[30m',	# Black
	'1': '\x1b[34m',	# Blue
	'2': '\x1b[32m',	# Green
	'3': '\x1b[36m',	# Cyan
	'4': '\x1b[31m',	# Red
	'5': '\x1b[35m',	# Purple
	'6': '\x1b[33m',	# Gold
	'7': '\x1b[37m',	# Light Gray
	'8': '\x1b[90m',	# Dark Gray
	'9': '\x1b[96m',	# Light Blue
	'a': '\x1b[92m',	# Light Green
	'b': '\x1b[96m',	# Light Cyan
	'c': '\x1b[91m',	# Light Red
	'd': '\x1b[95m',	# Light Purple
	'e': '\x1b[93m',	# Yellow
	'f': '\x1b[97m',	# White
	'l': '\x1b[1m',		# Bold
	'o': '\x1b[3m',		# Italic
	'n': '\x1b[4m',		# Underline
	'm': '\x1b[9m',		# Strikethrough
	'r': '\x1b[0m',		# Reset
	'k': '\x1b[22m',	# Normal intensity
}


def color_message(text: str) -> str:
	"""
	Converts custom color codes to ansi color codes
	Color codes can be called using the & symbol or the § symbol
	Example: &1Hello §2World
	"""
	return re.sub(
		r'§[0-9a-fk-or]|&[0-9a-fk-or]',
		lambda match: colors.get(match.group(0)[1], match.group(0)),
		text
	) + '\x1b[0m'


def printc(text: str) -> None:
	"""
	Prints a colored message to the console
	"""
	print(color_message(text))


def clear_color_codes(text: str) -> str:
	"""
	Removes all color codes from a string
	Color codes can be called using the & symbol or the § symbol
	Example: &1Hello §2World
	"""
	return re.sub(r'§[0-9a-fk-or]|&[0-9a-fk-or]', '', text)


def cstring(text: str) -> str:
	"""
	Replaces custom color codes in a string for their respective ANSI codes
	Stands for "Colored String"
	"""
	return color_message(text)