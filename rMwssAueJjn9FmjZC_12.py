
import collections
def number_pairs(txt):
    lon = txt.split()
    cnts = collections.Counter(lon[1:])
    return sum([v//2 for k,v in cnts.items()])

