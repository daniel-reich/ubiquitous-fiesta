
def twins(age, distance, velocity):
    jill = distance/velocity * 2
    jack = jill * (1 - velocity**2)**0.5
    return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(age + jack, age + jill)

