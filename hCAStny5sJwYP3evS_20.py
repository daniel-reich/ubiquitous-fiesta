
from re import finditer as find
def is_early_bird(_range, n):
    natural = sum(len(str(i)) for i in range(n-1))
    matches = find('(?=' + str(n) + ')', ''.join(map(str, range(_range +1)))) 
    indices = (match.start() for match in matches)
    ranges = [list(range(a, a + len(str(n)))) for a in indices]
    return ranges + (['Early Bird!'] if ranges[0][0] < natural else [])

