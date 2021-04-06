
def count_digits(lst, t):
    result = []
    total = 0
    digits = [list(str(n)) for n in lst]
    for number in digits:
        for digit in number:
            if t == "even" and int(digit) % 2 == 0:
                total += 1
            elif t == "odd" and int(digit) % 2 != 0:
                total += 1
        result.append(total)
        total = 0
    return result

