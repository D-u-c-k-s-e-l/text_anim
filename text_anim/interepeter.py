"""text_anim.interepeter

This module contains the `interpret` function, which interprets a
text animation.
"""

from time import sleep
from text_anim.graphics import go_to_location

def interpret(text: str):
	"""Interprets a text animation.

	Parameters:
	- `text` (str): The animation to interpret.

	Explanation:
		Each line of the animation is interpreted as follows:
		If the line starts with `#`, it is ignored.
		If the line starts with `:`, it is interpreted as a draw command.
		The draw command has the following format: `:x,y lines` where it
		draws the next `lines` lines at the location `(x, y)`.
		If the line starts with `!`, it is interpreted as a sleep command.
		The sleep command has the following format: `!seconds` where it
		sleeps for `seconds`.
		Any other line does nothing.
	"""
	lines = text.split('\n')
	mode = 'normal'
	lines_remaining = 0
	for line in lines:
		if mode == 'normal':
			if line == '':
				continue
			if line[0] == '#':
				continue
			if line[0] == ':':
				lines_remaining = int(line.split(' ')[1])
				x, y = line[1:].split(',')
				x = int(x)
				y = int(y)
				go_to_location((x, y))
				mode = 'draw'
			if line[0] == '!':
				sleep(float(line[1:]))
		if mode == 'draw':
			lines_remaining -= 1
			print(line, (0, 0))
			if lines_remaining <= 0:
				mode = 'normal'

def interpret_file(filename: str):
	"""Interprets a text animation from a file.

	Parameters:
	- `filename` (str): The file to interpret.

	Explanation:
		Each line of the animation is interpreted as follows:
		If the line starts with `#`, it is ignored.
		If the line starts with `:`, it is interpreted as a draw command.
		The draw command has the following format: `:x,y lines` where it
		draws the next `lines` lines at the location `(x, y)`.
		If the line starts with `!`, it is interpreted as a sleep command.
		The sleep command has the following format: `!seconds` where it
		sleeps for `seconds`.
		Any other line does nothing.
	"""
	with open(filename, encoding='utf-8') as file:
		interpret(file.read())

