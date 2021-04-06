
def worded_math(equ):
    dic = {"zero":0, "one":1, "two":2, 0:"Zero", 1:"One", 2:"Two"}
    lst = equ.split(" ")
    if lst[1].lower() == "plus":
        return dic[dic[lst[0].lower()]+dic[lst[2].lower()]]
    else:
        return dic[dic[lst[0].lower()]-dic[lst[2].lower()]]

