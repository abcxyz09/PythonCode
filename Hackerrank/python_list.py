
if __name__ == '__main__':
   N = int(raw_input())
   list = []
   for x in xrange(N):
       n = raw_input()
       splitList = n.split()
       if splitList[0] == 'insert':
          list.insert(int(splitList[1]),int(splitList[2]))
       elif splitList[0] == 'print':
          print list
       elif splitList[0] == 'remove':
          list.remove(int(splitList[1]))
       elif splitList[0] == 'reverse':
          list.reverse()
       elif splitList[0] == 'sort':
          list.sort()
       elif splitList[0] == 'pop':
          list.pop()
       elif splitList[0] == 'append':
          list.append(int(splitList[1])) 