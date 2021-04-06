
import re
def count_ones(l):
    return len(re.findall('1{2,}', ''.join([str(a) for a in l])))

