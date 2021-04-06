
def letter_check(lst):
    boolean = True
    for i in lst:
        for j in lst[1]:
            if j.lower() not in i.lower():
                boolean = False
    return boolean

