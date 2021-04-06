
from math import *
def check_perfect(num):
    list_of_divisors=[]
    for i in range(1,int(num/2)+1):
        if num%i==0:
            list_of_divisors.append(i)
    if sum(list_of_divisors)==num:
        return True
    else :
        return False

