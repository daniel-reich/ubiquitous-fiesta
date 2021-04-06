
def digits(number):
    length = len(str(number))
    fixed = sum((pos+1)*9*10**pos for pos in range(length))
    return fixed + (number - 10**length) * length

