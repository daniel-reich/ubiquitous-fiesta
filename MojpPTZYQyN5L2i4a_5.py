
def cars(wheels, bodies, figures):
    totalcars = 0
    check = True
    while check:
        if wheels >= 4 and bodies >= 1 and figures >= 2:
            wheels -= 4
            bodies -= 1
            figures -= 2
            totalcars += 1
        else:
            check = False
    return totalcars

