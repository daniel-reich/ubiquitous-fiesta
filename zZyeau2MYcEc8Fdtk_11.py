
from math import ceil
​
def round_number(num, n):
    eq = num / n
    return ceil(eq) * n if eq - round(eq) == 0.5 else round(eq) * n

