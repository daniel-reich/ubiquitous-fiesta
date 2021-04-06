
def sum_round(num):
    a = str(num)
    return ' '.join([str(int(a[0-i])*10**(i-1)) for i in range(1,len(a)+1) if a[0-i]!='0'])

