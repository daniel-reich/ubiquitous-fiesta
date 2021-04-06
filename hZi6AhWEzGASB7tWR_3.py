
check=lambda l:'decreasing'if all(x-y>0for x,y in zip(l,l[1:]))else'increasing'if all(x-y<0for x,y in zip(l,l[1:]))else'neither'

