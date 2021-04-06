
def digit_sum(n):
    return sum(map(int,','.join(str(n)).split(',')))
def root_digit(n):
    s = None
    return root_digit(digit_sum(n)) if len(str(n))> 1 else n

