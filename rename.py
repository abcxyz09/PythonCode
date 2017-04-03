import os
#path = "/media/jonyroy/Picture/SchoolFriends"


'''
def returnInteger(str):
    s=''
    t=False
    for x in xrange(len(str)):
    
        while str[x].isdigit():
            s+=str[x]
            x=x+1
            #print x
            t=True
        if t==True:
           break
    return s 
'''

count = 0
def fileName(path):
    global count
    if not os.path.isdir(path):
        print 'Dir not exist'
        return False
    else:
        li = os.listdir(path)
        for x in li:
            if os.path.isdir(path+'/'+x):
                fileName(path+'/'+x)
            else:
                if x.endswith('.jpg'):
                    count = count + 1
                #print 'File Name: ',x
    return count


#if os.path.isdir(path):

#    print 'The path exists'
#else:
#    print "The path doesn't exist"
#li=os.listdir(path)
#for x in li:
#   list = os.listdir(path + '/' +x)
#   print list
#print li
#uva='Lightoj-'
#for x in xrange(len(li)):
    
#    if li[x].endswith(".cpp") :
#       s=returnInteger(li[x])
#       if len(s)>1:
#          s1=path+'/'+li[x]
#          s2=path+'/'+uva+s+'.cpp'
#          os.rename(s1,s2)
           
#    elif li[x].endswith(".c") :
#       s=returnInteger(li[x])
#        if len(s)>1:
#           s1=path+'/'+li[x]
#           s2=path+'/'+uva+s+'.c'
#           os.rename(s1,s2)
#for x in xrange(len(li)):
#   if li[x].endswith('.o') :
#       s1=path+'/'+li[x]
#       os.remove(s1)
     
if __name__ == '__main__':
    path = raw_input('Enter The File Path >') 
    cnt = fileName(path)
    print 'Total Picture = ' ,cnt 