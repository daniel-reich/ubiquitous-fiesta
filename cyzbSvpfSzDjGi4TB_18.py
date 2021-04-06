
def harmonic(n):
    harmonic = 0
    for x in range(1, n+1):
        harmonic += 1 / x
    return round(harmonic, 3)

