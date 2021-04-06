
import math
def josephus(people):
    x = people - 2 ** math.floor(math.log2(people))
    if math.log2(people) % 1 == 0:
        return 1
    return 2 * x + 1

