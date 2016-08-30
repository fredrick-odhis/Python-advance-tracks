def is_Vowel(character):
	vowels = "AEIOUYaeiouy"
	if character in vowels:
	    return True
	else:
		return False

def position_of_first_vowel(word):
	i = 0
	for char in word:
		if is_Vowel(char) == True and (char != 'y' and i != 0):
			return i
		i = i + 1
	return -1

def pigify(word):
	i = 0
	for char in word:
		if is_Vowel(char) == True and (i == 0):
			new_word = word + '-way'
		elif is_Vowel(char) == False and (i == 0):
			w = word.pop(0)
			new_word = w + word + '-ay'
		return new_word
