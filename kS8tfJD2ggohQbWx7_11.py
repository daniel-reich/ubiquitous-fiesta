
def last_name_lensort(names):
​
​
    return sorted(names, key=lambda i: (len(i.split(' ')[1]),i[-1]))

