def solve(in_path):
	with open(in_path) as f:
		tests = f.readlines()
	for i in range(1, len(tests)):
		n, k = tests[i].split()
		n = int(n)
		k = int(k)
		max_l_r, min_l_r = choose_stall(n, k)
		print ("Case #%d: %d %d" % (i, max_l_r, min_l_r))

def choose_stall(n, k):
	stalls = [True] + [False] * n + [True]
	for i in range(k): # loop through persons
		candidates = []
		for j in range(len(stalls)): # loop through stalls
			if not stalls[j]: # if empty
				left = calculate_left_distance(stalls, j-1)
				right = calculate_right_distance(stalls, j+1)
				candidates.append((min(left, right), max(left, right), len(stalls)-j))
		candidates = sorted(candidates, reverse=True)
		selected = len(stalls) - candidates[0][2]
		# person i sits at the selected stall
		stalls[selected] = True

		# if last person
		if i == k-1:
			return (candidates[0][1], candidates[0][0])

def calculate_left_distance(stalls, i):
	dist = 0
	while i >= 0 and not stalls[i]:
		dist += 1
		i -= 1
	return dist

def calculate_right_distance(stalls, i):
	dist = 0
	while i < len(stalls) and not stalls[i]:
		dist += 1
		i += 1
	return dist

if __name__=='__main__':
	solve('C-small-2-attempt0.in')