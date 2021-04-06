
import math
def end_corona(recovers, new_cases, active_cases):
    x = recovers - new_cases
    y = math.ceil(active_cases / x)
    return y

