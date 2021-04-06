
import random
random.randrange = lambda x: random.random()
def manipulate():
    random.seed(0)
    res = random.random()
    random.seed(0)
    return res

