
def twins(age, distance, velocity):
    t = (2*distance)/velocity
    E = (1-velocity*velocity)**0.5
    a = round((t+age),1)
    b = round((age+E*t),1)
    return "Jack's age is {}, Jill's age is {}".format(b,a)

