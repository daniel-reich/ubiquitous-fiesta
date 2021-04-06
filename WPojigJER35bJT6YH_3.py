
def reversed_binary_integer(num):
    a=str(bin(num))
    b=a[2:][::-1]
    return int(b,2)

