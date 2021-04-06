
def prefix(exp):
  tmp=exp.split(' ')
​
  def go(tmp):
    #print(tmp,len(tmp))
    if len(tmp)<3: return tmp
    
    if len(tmp)>3:
      if (len(tmp[1])>1 or not tmp[1] in '+-/*') and (len(tmp[2])>1 or not tmp[2] in '+-/*'): 
        return go(tmp[0:3])  + tmp[3:] 
      return go([tmp[0]] +  go(tmp[1:])   )
    a=int(tmp[1])
    b=int(tmp[2])
    if tmp[0]=='+': return [str(a+b)]
    if tmp[0]=='*': return [str(a*b)]
    if tmp[0]=='-': return [str(a-b)]
    if tmp[0]=='/': return [str(a//b)]
​
​
​
  return int(go(tmp)[0])

