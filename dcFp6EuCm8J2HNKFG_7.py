
func=lambda l:len(l)+func([y for x in l if isinstance(x,list)and len(x)>0for y in x])if l else 0

