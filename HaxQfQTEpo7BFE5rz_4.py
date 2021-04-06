
alternate_pos_neg=lambda l:(l!=[0])*all(a*b<0for a,b in zip(l,l[1:]))

