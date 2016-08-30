def compounded_principal(time):
	P =  10000
	r =  0.08
	n =  1
	A = P * (1 + (r/n)) ** (n * time)
	return int(A)	
