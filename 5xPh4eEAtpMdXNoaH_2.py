
from collections import Counter
def longest_palindrome(s):
    one_odd, count = False, 0
    for v in Counter(s).values():
        if v % 2:
            count += v - 1
            if not one_odd:
                one_odd = True
        else:
            count += v
    return count + one_odd

