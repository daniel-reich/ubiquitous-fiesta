
import math
​
def twins(age, distance, velocity):
    t_jill = 2 * distance / velocity
    t_jack = t_jill * math.sqrt(1 - velocity**2)
    age_jill = round(age + t_jill, 1)
    age_jack = round(age + t_jack, 1)
    return "Jack's age is " + str(age_jack) + ", Jill's age is " + str(age_jill)

