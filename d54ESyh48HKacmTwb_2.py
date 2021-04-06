
from fractions import gcd as gcd_lib
def gcd(arr):
    gcd_num = gcd_lib(arr[0], arr[1])
    for n in arr[2:]:
        gcd_num = gcd_lib(gcd_num, n)
    return gcd_num

