
from re import findall
def negative_sum(chars):
    return sum(map(int, findall(r'-\d+', chars)))

