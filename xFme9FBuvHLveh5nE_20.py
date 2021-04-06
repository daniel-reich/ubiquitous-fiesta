
def is_zygodrome(num):
    l = 'X'+str(num)+'X'
    return sum(0 if l[i] == l[i+1] or l[i+1] == l[i+2] else 1 for i in range(len(l)-2)) == 0

