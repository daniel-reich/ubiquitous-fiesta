
def inclusive_list(start_num, end_num):
    mylist = []
    if start_num > end_num:
        return [start_num]
    else:
        for num in range(start_num, end_num + 1):
            mylist.append(num)
        return mylist

