
def is_pandigital(num):
    return "0123456789" ==  "".join(sorted(list(set(str(num)))))

