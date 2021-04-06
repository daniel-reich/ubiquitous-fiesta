
def delete_occurrences(lst, num):
    lst = lst[::-1]
    for i in lst:
        if lst.count(i) > num:
            for k in range(lst.count(i)-num):
                 lst.remove(i)
    return lst[::-1]

