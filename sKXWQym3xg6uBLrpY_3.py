
def iqr(lst):
    lst.sort()
    edge = len(lst) // 2
    return middle(lst[-edge:]) - middle(lst[:edge])
​
def middle(lst):
    if len(lst) % 2 != 0:
        return lst[len(lst) // 2] 
    return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

