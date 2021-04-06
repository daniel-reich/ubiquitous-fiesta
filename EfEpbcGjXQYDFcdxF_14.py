
def filter_list(l):
    mylist = []
    for item in l:
        try:
            mylist.append(int(item))
        except:
            continue;
    return mylist

