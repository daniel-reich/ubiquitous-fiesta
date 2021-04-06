
def simple_check(a, b):
    j= 0
    while(a!=0 and b!=0):
        if a%b ==0 or b%a==0:j+=1
        a-=1
        b-=1
    return j

