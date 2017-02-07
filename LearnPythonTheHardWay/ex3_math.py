# Date: 06-02-2017
# In This Program We will do some math calculation using Python
print "Addition", 10 + 20 * 2
print ( 10 + 20 ) * 2
cnt = 43 % 7 # % sign represent modulus.
print "Floating Modulus %s" %cnt

cnt = 43.5 % 7.
print type(cnt) # find out the type of the cnt.
print "%f" %cnt # floating point
print "%d" %cnt # integer number

ty = type(cnt)
print type(ty)
print "%r" %cnt # raw data

cnt = 10 >= 5
print type(cnt)
print "%d" %cnt

# Division Operation
print "integer division part one" , 19/5     # you have to use comma here.
print "integer division part two %d" %(19/5) # you can't use comma here.

print "floating Division part one" , (10./3) # use dot for floating division
print "floating division part two %f" %(10./3)

print "precedence", 7*5./3
print "precedence = " , 7 * (5./3)
print "precedence = " , (7 * 5.) / 3
