if __name__ == '__main__':
    from operator import itemgetter
    #list = [[10,3],[4,2],[6,5],'wewe']
    #list.sort(key = itemgetter(1),reverse = False)
    li = []
    number = int(raw_input())
    for x in xrange(number):
        #name = raw_input()
        #grade = float(raw_input())
        li.append([raw_input(),float(raw_input())])
    li.sort(key = itemgetter(1))
    list = []
    secondMinimum = 0.0
    minimum = li[0][1]
    for x in li:
        if x[1] > minimum:
            secondMinimum = x[1]
            break
    #print secondMinimum
    for x in li:
        if x[1] == secondMinimum:
            list.append(x[0])
    list.sort()
    for x in list:
        print x