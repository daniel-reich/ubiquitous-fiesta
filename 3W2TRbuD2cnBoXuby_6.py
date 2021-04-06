
collect=f=lambda s,n:[]if len(s)<n or len(s)==0else sorted([s[:n]]+f(s[n:],n))

