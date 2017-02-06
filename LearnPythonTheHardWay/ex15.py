from sys import argv
scriptName,fileName = argv # unpacking variables
print type(argv)
text = open(fileName)
print fileName
print scriptName
print text.read()
text.close()
print "Type FileName:"
fn=raw_input("> ")
text = open(fn)
print text.read()
print "adsfdfdffffff"
text.close()
