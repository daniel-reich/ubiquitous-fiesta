
def check_pattern(lst, pattern):
    if len(lst) == 0:
        return True
    dict = {str(lst[0]): pattern[0]}
    for i in range(1, len(lst)):
        print(i)
        if str(lst[i]) in dict.keys():
            if dict[str(lst[i])] != pattern[i]:
                return False
        else:
            if pattern[i] in list(dict.values()):
                return False
            dict[str(lst[i])] = pattern[i]
    return True

