
def my_sub(y, x):
    while y != 0:
        borrow = (~x) & y 
        x = x ^ y 
        y = borrow << 1
    return x

