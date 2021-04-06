
def delete_occurrences(lst, num):
    for i in lst:
        occ = lst.count(i)
        while occ > num:
            lst.reverse()
            lst.remove(i)
            lst.reverse()
            occ = occ - 1
    return lst
​
​
print(delete_occurrences([13, True, 13, None], 1))

