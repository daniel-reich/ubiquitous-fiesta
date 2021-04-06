
from math import sqrt
def twins(age,distance,velocity):
    te=2*distance/velocity
    jill=age+round(te,1)
    jack=age+round(te*sqrt(1-velocity**2),1)
    ans="Jack's age is {}, Jill's age is {}"
    return ans.format(jack,jill)

