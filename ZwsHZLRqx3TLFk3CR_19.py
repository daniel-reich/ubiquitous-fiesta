
from math import factorial
def eval_factorial(lst):
    ev=0
    for i in lst:
        if i =="0!" or i== "1! ":
            ev+=1
        else:
            ev+=factorial(int(i.strip("!")))
    return ev

