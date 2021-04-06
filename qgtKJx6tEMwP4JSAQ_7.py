
import math
def twins(age, distance, velocity):
    jill_age = age + 2 * distance / velocity
    jack_age = age + 2 * distance / velocity * math.sqrt(1 - velocity * velocity)
    result = [round(jack_age,1), round(jill_age,1)]
    return "Jack's age is " + str(result[0]) + ", Jill's age is " + str(result[1])

