
from itertools import accumulate
def distance_to_nearest_vowel(txt):
    def dist_to_last(txt):
        normalized = [0 if char in 'aeiou' else 1 for char in txt]
        return list(accumulate([normalized[0]*999]+normalized[1:], lambda a,b: (a+1)*b))
    return [min(to_last, to_next) for to_last, to_next in zip(dist_to_last(txt), reversed(dist_to_last(reversed(txt))))]

