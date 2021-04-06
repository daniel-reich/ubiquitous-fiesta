
import math
def century(year):
    c = math.ceil(year/100)
    return str(c)+"th century" if c<21 else str(c)+"st century"

