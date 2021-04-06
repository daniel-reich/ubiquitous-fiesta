
def square_digits(n):
    new = []
    for i in str(n):
        new.append(str(int(i) * int(i)))
    return int(''.join(new))

