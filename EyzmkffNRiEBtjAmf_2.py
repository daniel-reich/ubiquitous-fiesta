
does_brick_fit=lambda a,b,c,*z:min(a,b,c)<=min(z)and sorted([a,b,c])[1]<=max(z)

