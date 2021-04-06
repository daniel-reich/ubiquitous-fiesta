
gcd = lambda x,y: gcd(y,x%y) if y else x; lcm = lambda x,y: x*y/gcd(x,y)
lcm_of_list=lol=lambda n:lcm(lol(n[1:]),n[0]) if len(n)>1 else n[0]

