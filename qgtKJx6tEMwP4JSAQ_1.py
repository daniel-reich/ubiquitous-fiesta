
def twins(age, distance, velocity):
    t_e=2*distance/velocity
    t_o=t_e*(1-(velocity)**2)**0.5
    return "Jack's age is {}, Jill's age is {}" .format(round(age+t_o,1),round(age+t_e, 1))

