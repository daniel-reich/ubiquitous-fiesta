
def is_sastry(number):
    a = int(str(number) + str(number+1)) ** (1/2)
    return a == round(a)

