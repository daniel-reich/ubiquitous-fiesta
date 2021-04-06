
def sign(a):
  if a==0:return 0
  return (a)//abs(a)
​
def radial(txt,s,f):
  return [txt +str(s-x*sign(s-f)) for x in range(abs(s-f)+1)]
​
def rotation(x,s,f):
  side_diff=abs(ord(s)-ord(f))
  if abs(ord(s)-ord(f)) >4:
    incr=-1
    side_diff=8-side_diff
  else: 
    incr=1
  return [ chr((ord(s)-ord('A')+(i+1)*incr)%8+ord('A'))+str(x) for i in range(side_diff)]
    
​
def spider_vs_fly(spider, fly):
  side=(1+1-2**0.5)**0.5
  side_diff=abs(ord(spider[0])-ord(fly[0]))
​
  if side_diff>4:side_diff=8-side_diff
  s=int(spider[1])
  f=int(fly[1])
  sf=min(s,f)
​
  if sf*side_diff*side + abs(s-f) < s+f: # side way shorter than over A0
    if s>=f:
      out=radial(spider[0],s,f)+rotation(f,spider[0],fly[0])
    else:
      out=[spider] + rotation(s,spider[0],fly[0])
      out.pop()
      out+=radial(fly[0],s,f)
  else: # over A0
    out=radial(spider[0],s,1) + ["A0"] + radial(fly[0],1,f)
      
  return('-'.join(out))

