import string
import random

class Password:
	
	def __init__(self, charset, length):
		self.charset = charset
		self.length = length
		self.char_array = []
		self.password = []
	
	def set_charset(self):
		
		if ('l' in self.charset):
			self.char_array.append(string.ascii_lowercase)
		if ('u' in self.charset):
			self.char_array.append(string.ascii_uppercase)
		if ('s' in self.charset):
			self.char_array.append(string.punctuation)
		if ('d' in self.charset):
			self.char_array.append(string.digits)
	
	def get_char_array(self):
		
		print(self.char_array)
	
	def generate_password(self):
		
		for i in range(self.length):
			outer_idx = random.randrange(0, len(self.char_array))
			inner_idx = random.randrange(0, len(self.char_array[outer_idx]))
			self.password.append(self.char_array[outer_idx][inner_idx])
	
	def get_password(self):
		
		return ''.join(self.password)