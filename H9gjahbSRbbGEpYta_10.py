
def multiply(n1, n2):
    product = 0
    for i in range(abs(n1)):
        product += n2
    if n1 < 0:
        product = -product
    return product

