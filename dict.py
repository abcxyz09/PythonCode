import operator
dict = {'f':100, 'c':54,'b':78,'a':87,'e':45,'d':657}

print sorted(dict) # sorting with respect to keys
print sorted(dict.items(),reverse = True)
print sorted(dict.items())
print dict.keys() # print all keys
print dict.values() # print all values
b = sorted(dict.items(),key = operator.itemgetter(1),reverse = False)
print b[0]