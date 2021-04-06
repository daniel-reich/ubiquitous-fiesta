
def holey_sort(lst):
    return sorted(lst, key=holes)
​
def holes(x):
    cnt = 0
    for i in str(x):
        if i in '4690':
            cnt +=1
        if i == '8':
            cnt +=2
    return cnt

