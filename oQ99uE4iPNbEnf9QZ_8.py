
import sys
sys.setrecursionlimit(10**6)
​
def no_perms_digits(num, i=0, total=1):
    if i == num:
        if total // 10 == 0:
            return 1
        else:
            return 1 + no_perms_digits(num, i, total // 10)
    else:
        return no_perms_digits(num, i + 1, total * (i + 1))

