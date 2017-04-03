import time
li = [2,4,5,2,3,4,5,1,1,1,1,3,3,4,4,5,5,5,6,7,7,8,8,8,8,8,8,8,8,8,9,9,9,6,5,5,4,4,3,3,2,3,3,4,4,4,4,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
list = []
dict = {}
start_time = time.time()
for x in li:
	if not x in dict:
		list.append(x)
		dict[x] = 1
total = time.time() - start_time
print total
start = time.time()
l = []
for x in li:
	if x not in l:
		l.append(x)
total1 = time.time() - start
print total1
print total1 - total
list.sort()
print list
print dict