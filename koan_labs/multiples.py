def multiple_sum():
	i = 1
	listvalues = []
	while i < 1000: 
		if i % 3 == 0:
			listvalues.append(i)
		elif i % 5 == 0:
			listvalues.append(i)
		i += 1

	#print listvalues

	print sum(listvalues)
	return sum(listvalues)
	
multiple_sum()