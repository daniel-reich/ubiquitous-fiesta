
def rearranged_difference(num):
    upper = sorted(list(str(num)),reverse=True)
    lower = sorted(list(str(num)))
​
    upper_int = int(''.join(upper).lstrip('0'))
    lower_int = int(''.join(lower).lstrip('0'))
​
    return upper_int - lower_int

