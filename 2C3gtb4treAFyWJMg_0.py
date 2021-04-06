
def polybius(t):
  f=lambda d,v:list(d.keys())[list(d.values()).index(v)]if v!='24'else'I'
  d={y:'%s%s'%(i,j)for i,x in enumerate(['ABCDEFGHIKLMNOPQRSTUVWXYZ'[i:i+5]for i in range(0,25,5)],1)for j,y in enumerate(x,1)}
  d['J']=d['I']
  return' '.join(''.join(f(d,x[i:i+2])for i in range(0,len(x),2))for x in t.split()).lower()if t[:2].isdigit()else' '.join(''.join(d[y]for y in x if y.isalpha())for x in t.upper().split())

