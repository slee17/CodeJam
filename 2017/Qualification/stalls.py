import time

from collections import defaultdict

def solve(in_path, debug=False):
	start = time.time()
	
	with open(in_path) as f:
		tests = f.readlines()
	
	for i in range(1, len(tests)):
		n, k = tests[i].split()
		n = int(n)
		k = int(k)
		# max_l_r, min_l_r = choose_stall(n, k)
		# max_l_r, min_l_r = calculate_max_min(n, k)
		# max_l_r, min_l_r = calculate_max_min_dp(n, k)
		max_l_r, min_l_r = calculate_max_min(n, k)
		print ("Case #%d: %d %d" % (i, max_l_r, min_l_r))
	
	end = time.time()
	if debug:
		print ("Total time taken: ", end-start)

def calculate_max_min_recursive(n, k):
	if k == 1:
		return int(n/2), n - int(n/2) - 1
	left = calculate_max_min_recursive(n - int(n/2) - 1, int(k/2))
	right = calculate_max_min_recursive(int(n/2), k-int(k/2))
	return max(left, right)

def calculate_max_min(n, k):
	return calculate_max_min_cache(n, k, {})

def calculate_max_min_cache(n, k, cache):
	if (n, k) in cache:
		return cache[(n, k)]

	if k == 1:
		return int(n/2), n - int(n/2) - 1

	left = calculate_max_min_cache(n - int(n/2) - 1, int(k/2), cache)
	cache[(n - int(n/2) - 1, int(k/2))] = left

	right = calculate_max_min_cache(int(n/2), k-int(k/2), cache)
	cache[(int(n/2), k-int(k/2))] = right

	return max(left, right)

def calculate_max_min_dp(n, k):
	# initialize the dp table
	dp_table = [[(-float('inf'), -float('inf')) for i in range(n+1)] for j in range(k+1)]

	# fill in the base cases
	for i in range(n+1):
		dp_table[1][i] = (int(i/2), i-int(i/2)-1)
		# print (dp_table)

	for col in range(1, n+1):
		for row in range(2, min(col+1, k+1)):
			# print (col-int(col/2)-1, int(row/2))
			# print (int(col/2), row-int(row/2))
			# print (row, col)
			dp_table[row][col] = max(dp_table[int(row/2)][col-int(col/2)-1],
										dp_table[row-int(row/2)][int(col/2)])
			# print (dp_table)

	return dp_table[k][n]

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
	solve('C-large-practice.in')
	# solve('test.txt')