def print_two(*args):
	'''
	*args tells the python to take all the arguments to the function then 
	put them in args as a list.
	'''
	arg1,arg2=args # Unpacking list
	print "arg1 = %r, arg2 = %r" %(arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1=%r , arg2=%r" %(arg1,arg2)
print_two('Jony Roy',[100,1,2,3,4,2,4,2,'dfdfdf'])
print_two_again(('dfdsf',3334),[2,5,3,3,5,5,5,5,5,5,5])