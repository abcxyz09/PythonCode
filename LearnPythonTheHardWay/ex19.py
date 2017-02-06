def StudentAndTeacher(noofstudent,noofteacher):
	print "There are %d students in Dept." %noofstudent
	print "There are %d Teachers in Dept." %noofteacher

print "We can just give the function numbers directly."
StudentAndTeacher(50,10)

print "OR We can use variables from our script."
noofstudent=int(raw_input("Enter Student No:"))
noofteacher=int(raw_input("Enter Teacher No:"))
StudentAndTeacher(noofstudent,noofteacher)

print "we can even do math inside too:"
StudentAndTeacher(40+10,5*20/5)

print "And we can combine the two, variables and math:"
StudentAndTeacher(noofstudent+10,noofteacher+54)

StudentAndTeacher((78/7*8-9+7),74)