
list = [2,3,5,7,11	,'q',]
print list
#Append Method
list.append(29)
print list

list.append([31])
print list
list.append([37,41,47,53])
print list


#Extend Method
list.extend([3,8,7])
print list
list.extend('r')
print list
#Extend method argument must be an iterable eg. list,dict,turple,string,set
list.extend((7,8,9,9))
print list
list.extend({4:3,6:4})
print "dict added = %r" %(list)

li = sorted(list)
print list
print li
list.sort()
print list


dict = {'a':'gg'}
print dict['a']

list = [7,8,9]
print list, '\n'