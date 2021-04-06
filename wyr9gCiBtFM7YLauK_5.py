
g=3600
def time_sum(t):
 r=0
 for e in t:h,m,s=map(int,e.split(":"));r+=g*h+60*m+s
 return[r//g,r%g//60,r%60]

