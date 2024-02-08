from typing import Self
import re

def height(text: str) -> int:
	return TextBuilder(text).height()

def width(text: str) -> int:
	return TextBuilder(text).width()

def dimensions(text: str) -> tuple[int, int]:
	return TextBuilder(text).dimensions()

def num_of_s(text: str, look_for: str) -> int:
	return TextBuilder(text).num_of_s(look_for)

def num_of_r(text: str, look_for: str) -> int:
	return TextBuilder(text).num_of_r(look_for)

def indent(text: str, indent: str='\t') -> str:
	return TextBuilder(text).indent(indent)                      .get_text()

def outdent(text: str, outdent: str) -> str:	
	return TextBuilder(text).outdent(outdent)                    .get_text()

def fill(text: str) -> str:
	return TextBuilder(text).fill()                              .get_text()

def strip_newline_at_end(text: str) -> str:	
	return TextBuilder(text).strip_newline_at_end()              .get_text()

def ensure_newline_at_end(text: str) -> str:
	return TextBuilder(text).ensure_newline_at_end()             .get_text()

class TextBuilder:
	def __init__(self, text: str) -> None:
		self.text = text

	def height(self) -> int:
		"""Returns the number of lines in the text.

		Returns:
		- (int): The number of lines in the text.
		"""
		return self.ensure_newline_at_end().num_of_s('\n')

	def width(self) -> int:
		"""Returns the width of the text (int). If line lengths vary,
		the length of the longest line will be returned.

		Returns:
		- (int): The width of the text.
		"""
		return max([len(i) for i in self.text.split('\n')])

	def dimensions(self) -> tuple[int, int]:
		"""Returns the dimensions of the text (width: int, height: int).
		
		Returns:
		- (tuple(int, int)): The dimensions of the text.
		"""
		return self.width(), self.height()

	def num_of_s(self, look_for: str) -> int:
		"""Returns the number of times the string `look_for` appears
		in the text.

		Parameters:
		- `look_for` (str): The string to search for.

		Returns:
		- (int): The number of times `look_for` appears in the text.
		"""
		return len(self.text.split(look_for)) - 1

	def num_of_r(self, look_for: str) -> int:
		"""Returns the number of times the regex `look_for` appears
		in the text.

		Parameters:
		- `look_for` (str): The regex to search for.

		Returns:
		- (int): The number of times `look_for` appears in the text.
		"""
		return len(re.findall(look_for, self.text))

	def indent(self, indent: str='\t') -> Self:
		"""Returns a copy of the text with each line indented by
		`indent`.

		Parameters:
		- `indent` (str, optional): The string to indent each line with.
			Default is '\t'.
		"""
		return TextBuilder('\n'.join([
			f"{indent}{i}" for i in self.text.split('\n')
		]))

	def outdent(self, outdent: str) -> Self:
		"""Returns a copy of the text with each line followed by
		`outdent`.

		Parameters:
		- `outdent` (str): The string to outdent each line with.
		"""
		return TextBuilder('\n'.join([
			f"{i}{outdent}" for i in self.text.split('\n')
		]))

	def fill(self) -> Self:
		"""Returns a copy of the text with each line filled with spaces
		to the width of the text.
		"""
		text_width = self.width()
		return TextBuilder('\n'.join([
			f"{i:<{text_width}}"
			for i in self.text.split('\n')
		]))
	
	def strip_newline_at_end(self) -> Self:
		"""Returns a copy of the text with the newline at the end
		removed if it exists.
		"""
		if self.text == '': return TextBuilder(self.text)
		if self.text[-1] == '\n':
			return TextBuilder(self.text[:-1])
		return TextBuilder(self.text)
	
	def ensure_newline_at_end(self) -> Self:
		"""Returns a copy of the text with a newline at the end if
		there isn't one.
		"""
		if self.text[-1] != '\n':
			return TextBuilder(self.text + '\n')
		return TextBuilder(self.text)

	def get_text(self) -> str:
		"""Returns the text as a string
		
		Returns:
		- (str): The text.
		"""
		return self.text

	def __str__(self) -> str:
		return self.text
	
	def __repr__(self) -> str:
		return f"<TextBuilder '{self.text}'>"
	
	def __iter__(self):
		return self.strip_newline_at_end().get_text().split('\n')