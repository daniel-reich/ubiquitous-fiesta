
from string import punctuation as p
def kix_code(addr):
    _, last, first = addr.split(', ')
    start = [i for i,x in enumerate(last) if x.isdigit()][0]
    last = ''.join(['X' if x in p or x in ' ' else x for x in last[start:]])
    return '{}{}'.format(first[:8], last).replace(' ', '').upper()

