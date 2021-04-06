
def twins(age, distance, velocity):
    totalTime = (distance/velocity)*2
    jill =  round(age + totalTime,1)
    jack = round(age + totalTime- totalTime*(1-(1- velocity**2)**0.5),1)
    return "Jack's age is {}, Jill's age is {}".format(jack,jill)

