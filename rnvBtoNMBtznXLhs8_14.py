
def max_lst(lst):
    return sorted(lst)[::-1][:2]
​
def win_round(lst1,lst2):
    return max_lst(lst1)>max_lst(lst2)

