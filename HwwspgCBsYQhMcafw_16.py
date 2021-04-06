
def super_digit(n:str, k:int):
    p = n*k
    if len(p) == 1:
        return int(p)
    else:
        s_digit = 0
        for digit in p:
            s_digit += int(digit)
        return super_digit(str(s_digit), 1)

