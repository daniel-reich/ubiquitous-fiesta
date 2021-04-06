
def delete_occurrences(lst, num):
    lst.reverse()
    for item in lst:
        while (lst.count(item) > num):
            lst.remove(item)
    lst.reverse()
    return lst

