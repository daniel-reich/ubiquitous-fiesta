
def pad(m):l=len(m);return m[:140]if l>139else'%s%s%sl'%(m,' '*(l%2<1),'lo'*((140-l)//2+l%2-1))

