
def lucky_seven(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 7:
                    return True
    return False

