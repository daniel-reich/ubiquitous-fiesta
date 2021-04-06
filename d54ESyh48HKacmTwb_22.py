
f=lambda a,b:f(b,a%b)if b>0else a
gcd=lambda l,r=0:gcd(l[1:],f(r,l[0]))if l else r

