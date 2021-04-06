
import collections
def sock_merchant(lst):
    cnts = collections.Counter(lst)
    return sum([v // 2 for k,v in cnts.items()])

