
def consecutive_combo(lst1, lst2):
    l = lst1+lst2
    if sorted(l) == list(range(min(l),max(l)+1)):
        return True
    else:
        return False
​
​
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))

