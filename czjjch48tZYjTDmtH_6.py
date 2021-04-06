
def is_shifted(lst1, lst2):
    arr = []
    for i in range(len(lst1)):
        arr.append(lst2[i] - lst1[i])
​
    return len(set(arr)) == 1
​
​
def is_multiplied(lst1, lst2):
    arr = []
    for i in range(len(lst1)):
        arr.append(lst2[i] / lst1[i])
​
    return len(set(arr)) == 1

