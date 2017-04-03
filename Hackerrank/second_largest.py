if __name__ == '__main__':
	n = int(raw_input())
	m = raw_input()
	arr = [int(x) for x in m.split()]
	firstLargest = -1000
	secondLargest = -1000
	for x in arr:
		if x > firstLargest:
			firstLargest, secondLargest = x, firstLargest
		elif x < firstLargest and x > secondLargest:
			secondLargest = x
	print secondLargest
