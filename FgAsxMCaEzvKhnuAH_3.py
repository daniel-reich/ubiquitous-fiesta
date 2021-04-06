
from re import findall
def deep_sum(lst):
    return sum(list(map(int, findall("-?\d+", str(lst)))))

