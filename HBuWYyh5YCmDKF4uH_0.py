
from collections import*
almost_sorted=lambda l:min(Counter(x<y for x,y in zip(l,l[1:])).values())==1

