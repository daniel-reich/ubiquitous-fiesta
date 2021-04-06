
import math
​
def non_repeats(radix):
    ans = 0
    for d in range(1, radix + 1):
        # consider numbers of d digits:
        ans += (radix - 1) * math.factorial(radix - 1) // math.factorial(radix - d)
    return ans

