
import random
def manipulate():
    random.seed(1)
    global k
    x = random.randrange(1000 + k**10)
    random.seed(1)
    return x

