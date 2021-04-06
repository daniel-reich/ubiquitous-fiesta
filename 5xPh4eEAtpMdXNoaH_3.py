
from collections import Counter
​
def longest_palindrome(s):
    C = Counter(s)
    ans = 0
    odd = False
    for c in C.values():
        if c % 2 == 0:
            ans += c
        else:
            ans += c - 1
            odd = True
    return ans + (1 if odd else 0)

