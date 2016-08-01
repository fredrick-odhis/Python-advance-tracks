def largest_prime_factor(args):
	test_value = 2
	while args > 1:
		if args % test_value == 0:
			args /= test_value;
		else:
			test_value += 1
	return test_value

largest_prime_factor(47)
