
def count_number(lst):
    lst = str(lst)
    for x in "[],.":
        lst = lst.replace(x, "") 
    return sum([1 for x in lst.split() if x.isnumeric()])

