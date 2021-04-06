
def delete_occurrences(lst, num):
    lst_n = []
    for item in lst:
        if lst_n.count(item)<num:
            lst_n.append(item)
        else:
            continue
        
    return lst_n

