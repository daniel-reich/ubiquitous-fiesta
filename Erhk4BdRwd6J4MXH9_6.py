
def is_leap(year):
    if year % 400 == 0:
        x = 1
    else:
        x =0
    if year % 4 == 0 and year % 100 != 0 :
        y =1
    else:
        y = 0
    if x + y ==1:
        res = True
    else:
        res = False
    return res

