
def digits(number):
    l = len(str(number))
    return number * l - int('1' * l)

