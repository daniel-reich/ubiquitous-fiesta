
def total_points(guesses, word):
    points = {3 : 1, 4 : 2, 5 : 3, 6 : 54}
    total = 0
    for x in guesses:
        xl = list(x)
        for y in word:
            try:
                xl.remove(y)
            except ValueError:
                pass
        if len(xl) == 0:
            total += points[len(x)]
    return total

