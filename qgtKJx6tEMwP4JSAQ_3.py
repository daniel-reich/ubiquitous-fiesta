
def twins(age, distance, velocity):
    earth = 2 * distance / velocity
    ship = (1 - velocity ** 2) ** (1 / 2)
    jill = age + earth
    jack = age + earth * ship
    return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(jack, jill)

