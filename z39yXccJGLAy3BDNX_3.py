
def flipping_bits(n):
    x = "{:032b}".format(n)
    y = ['1' if i=='0' else '0' for i in x]
    y = "".join(y)
    return int(y, 2)

