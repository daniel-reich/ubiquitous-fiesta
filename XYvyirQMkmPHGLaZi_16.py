
def boom_intensity(n):
    res = "B" + "o" * n + "m"
    if n < 2:
        return "boom"
    elif n % 5 == 0 and n % 2 == 0:
        return res.upper() + "!"
    elif n % 5 == 0:
        return res.upper()
    elif n % 2 == 0:
        return res + "!"
    else:
        return res

