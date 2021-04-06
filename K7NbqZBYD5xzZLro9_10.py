
def sumdigits(nbr):
    exp = len(str(nbr))
    if exp == 0:
        return 0
    if exp == 1:
        return sum(range(1, nbr + 1  ) )
    digit = nbr//10**(exp-1)
    allnines = 45 * (exp - 1) * 10**(exp - 2) * digit
    firstdigits = sum(range(1, digit  ) ) * 10**(exp-1)
    results = allnines+firstdigits+ digit
    remaining_nbr = nbr - digit *10**(exp - 1) 
    results = results +   sumdigits(remaining_nbr) + remaining_nbr * digit
    return results
def digits_sum(start, stop):
    return sumdigits(stop) - sumdigits(start - 1)

