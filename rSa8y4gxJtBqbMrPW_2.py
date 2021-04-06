
gcd=lambda x,y:gcd(y,x%y)if y else x
lcm=lambda a,b:a*b/gcd(a,b)

