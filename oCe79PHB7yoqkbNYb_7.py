
def break_point(num):
    num = str(num)
    return any([sum(map(int,num[:i])) ==  sum(map(int,(num[i:]))) for i in range(1,len(num))])

