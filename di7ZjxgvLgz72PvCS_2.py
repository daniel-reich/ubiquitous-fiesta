
validate_swaps=lambda l,t:[sum(x!=y for x,y in zip(t,x))/2==1if set(t)==set(x)else 0for x in l]

