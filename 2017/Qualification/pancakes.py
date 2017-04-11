def solve(in_path):
	with open(in_path) as f:
		tests = f.readlines()
	for i in range(1, len(tests)):
		pancakes, k = tests[i].split()
		pancakes = list(pancakes)
		k = int(k)
		print (flip(pancakes, k, i))

def flip(pancakes, k, case_num):
	# base cases
	num_blanks = pancakes.count('-')
	if num_blanks == 0:
		return "Case #%d: 0" % case_num # we're done

	i = 0
	num_flips = 0
	while i < len(pancakes):
		if pancakes[i] == '+':
			i += 1
		elif i + k > len(pancakes): # can't flip
			return "Case #%d: IMPOSSIBLE" % case_num
		else:
			for j in range(k):
				pancakes[i+j] = '+' if pancakes[i+j] == '-' else '-'
			num_flips += 1
			i += 1

	return "Case #%d: %d" % (case_num, num_flips)

if __name__=='__main__':
	solve('A-large.in')