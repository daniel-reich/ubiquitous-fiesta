
def sum_fractions(lst):
    x=[]
    index=0
    sum = 0
    for i in lst:
        val= i[0]/i[1]
        x.insert(index,val)
        index=index+1
    for n in x:
        sum = sum + n;
    sum = round(sum)
    return sum

