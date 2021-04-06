
def lucky_seven(lst):
    len_lst = len(lst)
    if len_lst > 2:
        for i in range(len_lst - 2):
            for j in range(i + 1, len_lst - 1):
                for k in range(j + 1,  len_lst):
                    if lst[i] + lst[j] + lst[k] == 7:
                        return True
    return False

