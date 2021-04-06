
from itertools import*
combinator=lambda l,s='':l[0]if len(l)<2else[s.join(x)for x in(product(l[0],l[1])if len(l)<3else product(l[0],l[1],l[2]))]

