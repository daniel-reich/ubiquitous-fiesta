
def twins(age, distance, velocity):
    earth_time = 2 * distance / velocity
    ship_time = earth_time * (1 - velocity * velocity) ** 0.5
    return "Jack's age is {:.1f}, Jill's age is {:.1f}".format(age + ship_time,
                                                               age+earth_time)

