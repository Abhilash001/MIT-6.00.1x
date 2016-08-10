import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
	'''
	file_name (string): the name of the file containing 
	the list of words to load	

	Returns: a list of valid words. Words are strings of lowercase letters.

	Depending on the size of the word list, this function may
	take a while to finish.
	'''
	print 'Loading word list from file...'
	# inFile: file
	in_file = open(file_name, 'r', 0)
	# line: string
	line = in_file.readline()
	# word_list: list of strings
	word_list = line.split()
	print '  ', len(word_list), 'words loaded.'
	in_file.close()
	return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
	'''
	Determines if word is a valid word, ignoring
	capitalization and punctuation

	word_list (list): list of words in the dictionary.
	word (string): a possible word.
	
	Returns: True if word is in word_list, False otherwise

	Example:
	>>> is_word(word_list, 'bat') returns
	True
	>>> is_word(word_list, 'asdf') returns
	False
	'''
	word = word.lower()
	word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
	return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
	"""
	Returns: a joke in encrypted text.
	"""
	f = open("story.txt", "r")
	story = str(f.read())
	f.close()
	return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
	### DO NOT MODIFY THIS METHOD ###
	def __init__(self, text):
		'''
		Initializes a Message object
				
		text (string): the message's text

		a Message object has two attributes:
			self.message_text (string, determined by input text)
			self.valid_words (list, determined using helper function load_words
		'''
		self.message_text = text
		self.valid_words = load_words(WORDLIST_FILENAME)

	### DO NOT MODIFY THIS METHOD ###
	def get_message_text(self):
		'''
		Used to safely access self.message_text outside of the class
		
		Returns: self.message_text
		'''
		return self.message_text

	### DO NOT MODIFY THIS METHOD ###
	def get_valid_words(self):
		'''
		Used to safely access a copy of self.valid_words outside of the class
		
		Returns: a COPY of self.valid_words
		'''
		return self.valid_words[:]
		
	def build_shift_dict(self, shift):
		import string
		small=string.ascii_lowercase
		shift_dict={small[i]: small[(i+shift)%26] for i in range(26)}
		Capital=string.ascii_uppercase
		shift_dict.update({Capital[i]: Capital[(i+shift)%26] for i in range(26)})
		return shift_dict

	def apply_shift(self, shift):
		import string
		cipher_d = self.build_shift_dict(shift)
		encrypted_text = ""
		for letter in self.message_text:
			if letter in string.ascii_lowercase+string.ascii_uppercase:
				encrypted_text+=cipher_d[letter]
			else:
				encrypted_text+=letter
		return encrypted_text


class PlaintextMessage(Message):
	def __init__(self, text, shift):
		Message.__init__(self, text)
		self.shift = shift
		self.encrypting_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)

	def get_shift(self):
		return self.shift

	def get_encrypting_dict(self):
		return self.encrypting_dict.copy()

	def get_message_text_encrypted(self):
		return self.message_text_encrypted

	def change_shift(self, shift):
		self.shift = shift
		self.encrypting_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
	def __init__(self, text):
		Message.__init__(self, text)

	def decrypt_message(self):
		best_score, best_shift = 0, 0
		decrypted_message = ""
		for shift in range(25, 0, -1):
			decrypted_text = self.apply_shift(shift)
			decrypted_words = decrypted_text.split(' ')
			score = 0
			for word in decrypted_words:
				if is_word(self.valid_words, word):
					score+=1
			if score > best_score:
				best_score = score
				best_shift = shift
				decrypted_message = decrypted_text
		return (best_shift, decrypted_message)


#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
	
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()

def decrypt_story():
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()

print decrypt_story()[0]
print decrypt_story()[1]