
def bridge_shuffle(lst1, lst2):
​
    suffled_list, i = [], 0
​
    while True:
​
        if i >= len(lst1):
            return suffled_list + lst2[i:]
​
        if i >= len(lst2):
            return suffled_list + lst1[i:]
​
        suffled_list += [lst1[i]] + [lst2[i]]
​
        i += 1

