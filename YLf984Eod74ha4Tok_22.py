
def leap_year(yr):
    ret = ((yr%4)==0)
    ret1 = ((yr%100)==0)
    ret2=((yr%400)==0)
    retval1 = ((ret+ret1+ret2)!=2)
    retval2 = ((ret+ret1+ret2)==0)
    retval = (retval1+retval2)==1
    return retval
​
print(leap_year(2016))

