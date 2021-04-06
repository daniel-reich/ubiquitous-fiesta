
from collections import Counter
def sock_merchant(lst):
    return sum (count//2 for _, count in Counter(lst).most_common())

