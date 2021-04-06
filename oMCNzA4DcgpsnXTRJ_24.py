
def missing_num(lst):
    check = 1
    for num in lst:
        if check not in lst:
            continue
        check+=1
    return check

