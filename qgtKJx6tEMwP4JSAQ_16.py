
def twins(age, distance, velocity):
    multiplier = 1 / ((1 - velocity ** 2) ** (.5))
    jill = round((distance / velocity) * 2 + age, 1)
    jack = round((jill - age) / multiplier + age, 1)
    return "Jack's age is {}, Jill's age is {}".format(jack, jill)

