
def digit_count(n):
    digits = str(n)
    fina = []
    for i in list(digits):
        fina.append(str(digits.count(i)))
    return int("".join(fina))

