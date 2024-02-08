from text_anim.tools import TextBuilder
from time import sleep

def go_to_location(location: tuple[int, int]) -> str:
	"""Returns a string that moves the cursor to the given location.

	Parameters:
	- `location` (tuple(int, int)): The new location of the cursor.
		Location is in the form (x, y) where x is the column and y is
		the row.
	
	Returns:
	- (str): A string that moves the cursor to the given location.
	"""
	# ESC [ row ; col H
	return "\x1b[" + str(location[1] + 1) + ";" + str(location[0] + 1) + "H"

def render_text(text: str, location: tuple[int, int]):
	"""Renders text at the given location.
	"""
	text = TextBuilder(text).strip_newline_at_end().fill().get_text()
	new_text = ''
	for i, line in enumerate(text.split('\n')):
		line_location = (location[0], location[1] + i)
		new_text += go_to_location(line_location) + line
	print(new_text)

def clear_screen():
	"""Clears the screen.
	"""
	print("\x1b[2J")
