
def removeDups(list1):
    list2 = []
    for each in list1:
        if each not in list2:
            list2.append(each)
    return list2

