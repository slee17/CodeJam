def solve(in_path):
	with open(in_path) as f:
		tests = f.readlines()
	for i in range(1, len(tests)):
		n = int(tests[i])
		print ("Case #%d: %s" % (i, find_last_tidy(n)))

def find_last_tidy(n):
	# base case: a single digit number is always tidy
	if n < 10:
		return n

	n = list(str(n))
	i = 1

	while i < len(n):
		if int(n[i-1]) <= int(n[i]):
			# we're good so move on
			i += 1
		else:
			n[i-1] = str(int(n[i-1]) - 1)
			n[i:] = ['9'] * (len(n) - i)
			# return to the front and start again
			i = 1

	# drop leading zeros
	j = 0
	while j < len(n) and n[j] == '0':
		j += 1

	return ''.join(n[j:])

if __name__=='__main__':
	solve('B-large-practice.in')
	# solve('test.txt')