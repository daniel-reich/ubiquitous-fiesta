
import math
​
def choose(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
​
def dice_roll(n, outcome):
    if n > outcome or 6 * n < outcome:
        return 0
    ans = 0
    kmax = math.floor((outcome - n) / 6)
    for k in range(kmax + 1):
        ans += (-1)**k * choose(n, k) * choose(outcome - 6 * k - 1, outcome - 6 * k - n)
    return ans

