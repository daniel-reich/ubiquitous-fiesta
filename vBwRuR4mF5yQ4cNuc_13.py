
def count_missing_nums(lst):
    mylist = []
    for items in lst:
        try:
            mylist.append(int(items))
        except:
            continue
    mylist.sort()
    missing_items = 0
    start_count = mylist[0]
    end_count=mylist[len(mylist)-1]
    for item in range(start_count, end_count):
        if item in mylist:
            continue
        else:
            missing_items +=1
    return missing_items

