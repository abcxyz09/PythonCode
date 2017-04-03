'''
Python's default arguments are evaluated once 
when the function is defined,not each time the 
function is called.

Run the program you will see the difference.
'''
def append_to(element,li=[]): # Passing defaul argument
    li.append(element)
    return li

def append_to_1(element,li):
	li.append(element)
	return li
	 
my_list = append_to([7,8])
print  my_list,'\n'
my_list = append_to([4])
print my_list,'\n'

my_list = append_to_1([4,5,7],[9999])
print my_list , '\n'
my_list = append_to_1([8888,9999,4444],[7,8,7])
print my_list
print locals()
