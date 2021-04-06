
import math
​
def fruit_salad(fruits):
​
    final = []
    for fruit in fruits:
        name_len = len(fruit)
​
        if name_len%2 == 0:
            mid_point = int(name_len/2)
        else:
            mid_point = (name_len/2)
            mid_point = int(math.floor(mid_point))
​
        first_half = fruit[:mid_point]
        second_half = fruit[mid_point:]
​
        final.append(first_half)
        final.append(second_half)
​
    result = sorted(final)
​
    result = ''.join(result)
    return result

