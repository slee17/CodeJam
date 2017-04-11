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

	n = str(n)
	i = 1
	while i < len(n):
		if int(n[i-1]) <= int(n[i]):
			# we're good so move on
			i += 1
		else:
			# 10 is a special case
			if n[i-1] == '1':
				return '9' * (len(n) - 1)
			# if decreasing the digit currently in question
			# affects its relationship with the digit before
			if i >= 2 and int(n[i-1])-1 < int(n[i-2]):
				j = 0
				while int(n[i-1])-1 < int(n[i-j]):
					j += 1
				return n[:j] + str(int(n[i-2])-1) + '9' * (len(n) - j - 1)
			latest_tidy = n[:i-1] \
							+ str(int(n[i-1])-1) \
							+ '9' * (len(n) - i)
			return latest_tidy

	return n

if __name__=='__main__':
	solve('test.txt') # B-small-attempt2.in