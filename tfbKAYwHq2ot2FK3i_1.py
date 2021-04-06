
def non_repeats(radix):
    solution, factorial, maxi = 1, 1, radix - 1
    for i in range(maxi, 0, -1):
        factorial *= i
        solution += factorial
    return solution*maxi

