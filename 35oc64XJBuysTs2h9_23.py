
import math
​
def median(lst):
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        return round((lst[n//2] + lst[n//2-1]) / 2., 1)
    else:
        return lst[n//2]
​
def get_quartiles(lst, method):
    lst.sort()
    q0, q2, q4 = lst[0], median(lst), lst[-1]
    m = len(lst)
    if method in ["T", "MM"]:
        if m % 2 == 0:
            lower, upper = lst[:m//2], lst[m//2:]
        else:
            if method == "T":
                lower, upper = lst[:m//2+1], lst[m//2:]
            else:
                lower, upper = lst[:m//2], lst[m//2+1:]
        q1, q3 = median(lower), median(upper)
    else:
        # method "MS"
        n = (m + 1) / 4
        if n - int(n) == .5:
            n = math.ceil(n)
        else:
            n = int(round(n, 0))
        q1 = lst[n - 1]
        n = 3 * (m + 1) / 4
        if n - int(n) == .5:
            n = math.floor(n)
        else:
            n = int(round(n, 0))
        q3 = lst[n - 1]
    return [q0, q1, q2, q3, q4]

