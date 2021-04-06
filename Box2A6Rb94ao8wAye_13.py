
leader=lambda l:[x for i,x in enumerate(l)if all(x>y for y in l[i+1:])]

