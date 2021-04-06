
def is_zygodrome(n):
    '''
    Returns whether n is a zygodrome as defined in the instructions.
    '''
    count, n = 1, str(n)
​
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            count += 1
        else:
            if count < 2:
                return False
            count = 1
​
    return count > 1

