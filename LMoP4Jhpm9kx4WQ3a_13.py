
def is_ascending(astring):
    print(astring)
    if astring == '1235':
        print('')
    newlist = []
    for i in range(len(astring)):
        try:
            for j in range(0,len(astring),i):
                newlist.append(astring[j:j+i])
            if is_ascending_list(newlist):
                return True
            newlist = []
        except Exception as e:
            continue
    return False
            
def is_ascending_list(alist):
    for i in range(len(alist)-1):
        if int(alist[i+1]) > int(alist[i]) and int(alist[i+1]) - int(alist[i]) == 1:
            continue
        else:
            return False
    return True

