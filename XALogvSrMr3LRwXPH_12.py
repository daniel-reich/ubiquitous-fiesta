
is_shuffled_well=lambda l:1-any(x==y+1==z+2 or x==y-1==z-2for x,y,z in zip(l,l[1:],l[2:]))

