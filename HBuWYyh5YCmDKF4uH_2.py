
def almost_sorted(list):
    rev_list = sorted(list)
    rev_list.reverse()
    if list == sorted(list) or list == rev_list:
        return False
    for i in range(len(list)):
        test_list = list[:]
        test_list.pop(i)
        sorted_list2 = sorted(test_list[:])
        sorted_list2.reverse()
        sorted_list = sorted(test_list)
        if test_list == sorted_list or test_list == sorted_list2:
            return True
    return False

