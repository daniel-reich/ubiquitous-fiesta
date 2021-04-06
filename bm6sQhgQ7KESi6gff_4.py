
from collections import Counter
​
def find_the_difference(s, t):
    return (Counter(t) - Counter(s)).most_common()[0][0]

