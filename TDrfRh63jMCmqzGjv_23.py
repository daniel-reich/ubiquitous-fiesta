
def is_anti_list(lst1, lst2):
    if set(lst1)!=set(lst2): return False
    for i in range(len(lst1)):
        # print(lst1[i]," - ",lst2[i])
        if(lst1[i]==lst2[i]):
            return False
    return True

