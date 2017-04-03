# Python 3


def binaryTree(r):
	return [r,[],[]]

def insertLeftChild(root,newvalue):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newvalue,t,[]])
	else:
		root.insert(1,[newvalue,[],[]])

def insertRightChild(root,newvalue):
	t = root.pop(2)
	if len(t) > 1 :
		root.insert(2,[newvalue,t,[]])
	else:
		root.insert(2,[newvalue,[],[]])
r = binaryTree(4)
insertLeftChild(r,5)
insertLeftChild(r,10)
insertRightChild(r,20)
insertRightChild(r,50)
print(r,'\n',r[0],r[1],r[2])