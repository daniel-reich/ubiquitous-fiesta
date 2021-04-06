
from collections import Counter
​
​
def unique(lst):
    return Counter(lst).most_common()[-1][0]

