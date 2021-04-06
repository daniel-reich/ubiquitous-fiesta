
f=lambda l,s:[sum(x>y for y in(l[:i],l[i:])[s])for i,x in enumerate(l)]
left_side=lambda l:f(l,0)
right_side=lambda l:f(l,1)

