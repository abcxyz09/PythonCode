n = raw_input()
li = [if int(x) not in li for x in n.split(' ')]
n = raw_input()
list = [int(x) for x in n.split(" ")]
resultList = []
for x in li:
	if x in list:
		resultList.append(x)
print li
print list
print resultList