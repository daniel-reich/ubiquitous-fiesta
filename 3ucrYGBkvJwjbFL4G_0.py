
reversible_inclusive_list=f=lambda s,e:[s]if s==e else[s]+f(s+(1,-1)[s-e>0],e)

