
def complete_square(lst):
    if len(lst) == len(lst[0]):
        return lst
​
    while len(lst) != len(lst[0]):
​
        if len(lst)>len(lst[0]):
​
            for i in range(len(lst)):
​
                lst[i].append(0)
        else:
​
            for j in range(len(lst[0])-len(lst)):
​
                lst.append([0 for k in range(len(lst[0]))])
            
    return lst

