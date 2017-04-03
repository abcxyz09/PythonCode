
def count_substring(string, sub_string):
    cnt = 0
    loop = True
    pos = 0
    while loop:
        position = string.find(sub_string,pos)
        if position >= 0:
            cnt = cnt + 1
            loop = True
            pos = position + 1
        else:
            loop = False
        print position
    return cnt




if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count