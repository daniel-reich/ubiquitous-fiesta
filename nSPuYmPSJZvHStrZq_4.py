
def oddeven(lst):
    odd, even = 0, 0
    for n in lst:
        if n % 2:
            odd += 1
        else:
            even += 1
    return odd > even

