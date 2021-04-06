
def n_differences(lst):
​
    while True:
        temp = []
        for i, value in enumerate(lst):
            if i == len(lst) - 1:
                break
            temp.append(lst[i+1] - value)
​
        lst = temp[:]
        if len(lst) == 1:
            return lst[0]

