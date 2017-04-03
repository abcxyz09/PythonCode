
with open('text.txt','ab') as file:
    for x in xrange(1,3):
        name = raw_input('Enter Your Name >')
        age = raw_input('Enter Age >')
        file.write('Name : '+name + '\n')
        file.write('Age : ' + age + '\n')
        file.read()
    file.close()