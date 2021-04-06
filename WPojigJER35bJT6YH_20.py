
def reversed_binary_integer(num):
    a = bin(num)[2::][::-1]
    return int(a,2)

