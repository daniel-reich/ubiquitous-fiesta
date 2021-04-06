
def square_root(n):
    guess = int(pow(n, 0.5))
    while pow(guess, 2) != n:
        guess -= round((pow(guess, 2) - n) / guess / 2)
    return guess

