
def count_uppercase(lst):
    count = 0
    for i in lst:
        for j in i:
            if (j.isupper()) == True:
                count += 1
    return count

