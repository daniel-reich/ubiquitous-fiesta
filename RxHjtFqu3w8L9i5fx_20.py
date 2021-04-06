
import math
def bell(N):
    return round((1 / math.e) * sum([(k**N) / (math.factorial(k)) for k in range(999)]))

