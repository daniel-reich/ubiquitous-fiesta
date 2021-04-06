
def func(lst):
    if type(lst) == list:
        count = 0
        for i in range(len(lst)):
            count += func(lst[i]) + 1
        return count
    else:
        return 0

