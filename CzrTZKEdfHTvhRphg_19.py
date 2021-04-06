
def mixed_number(frac):
    num = int(frac[:frac.index("/")])
    if num == 0:
        return "0"
    den = int(frac[frac.index("/") + 1:])
    if den != 0:
        integer = abs(num) // den
        new_num = abs(num) % den
        for i in reversed(range(2, new_num + 1)):
            if new_num % i == 0 and den % i == 0:
                new_num //= i
                den //= i
​
    return_str = ""
    if new_num != 0:
        return_str = str(new_num) + "/" + str(den)
    if integer != 0:
        return_str = str(integer) + " " + return_str
        if new_num == 0:
            return_str = return_str[:-1]
    if frac[0] == "-":
        return "-" + return_str
    return return_str

