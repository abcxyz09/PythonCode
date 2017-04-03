class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def traverse(node):
    print(node.key)
    if node.leftChild is not  None:
    	traverse(node.leftChild)
    if node.rightChild is not  None:
    	traverse(node.rightChild)


r = BinaryTree('a')
#print(r.getRootVal())
#print(r.getLeftChild())
r.insertLeft('b')
r.insertRight('c')
r.insertLeft('d')
#print(r.getLeftChild())
#print(r.getLeftChild().getRootVal())
r.insertRight('e')
r.insertLeft('f')
r.insertRight('g')
#print(r.getRightChild())
#print(r.getRightChild().getRootVal())
#r.getRightChild().setRootVal('hello')
#print(r.getRightChild().getRootVal())
traverse(r)