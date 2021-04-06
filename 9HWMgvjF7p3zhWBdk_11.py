
def keys_and_values(d):
​
    key_lst = sorted(d)
​
    val_lst = []
​
    for item in key_lst:
​
        val_lst.append(d[item])
​
    return [key_lst,val_lst]

