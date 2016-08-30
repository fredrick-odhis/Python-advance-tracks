def count_letter_b(string):
		#counts the occurence of letter b in a string
	count = 0
	for x in string:
		if x == 'b' or x == 'B':
			count += 1
	return count
