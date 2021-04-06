
reversible_inclusive_list=lambda s,e:list(range(s,*((e+1,),(e-1,-1))[s>e]))

