
from itertools import product as P
def crack_pincode(pincode):
  d={'0':'08','1':'124','2':'1235','3':'236','4':'1457','5':'24568','6':'3569','7':'478','8':'05789', '9':'689'}
  A=[d[pincode[i]] for i in range(len(pincode))]
  return [''.join(x) for x in P(*A)]

