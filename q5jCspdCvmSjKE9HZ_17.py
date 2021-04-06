
from fractions import gcd
​
​
def lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // gcd(lcm, numbers[i])
    return lcm

