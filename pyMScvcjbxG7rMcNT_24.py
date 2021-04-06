
def sum_list(lst):
    s=lst[0]
    print("lst",lst)
​
    if(type(lst[0])==list):
        print("gh")
​
        s=sum_list(lst[0])
​
    if (len(lst) == 1):
        print("hel")
        return s
​
​
    return s + sum_list(lst[1:])

