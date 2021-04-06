
def c_cipher(msg,keyword):
  if " " in msg:
    key = [i for i in keyword]
    key.sort()
    order = [keyword.index(i) for i in key] 
    p = len(order)
    msg = "".join(i.lower() for i in msg if i.isalpha() or i.isnumeric())
    if len(msg)%p != 0:
      msg += (p-len(msg)%p)*"x"
    return "".join([msg[i+p*j] for i in order for j in range (len(msg)//p)])
  key = [i for i in keyword]
  key.sort()
  order = [key.index(i) for i in keyword] 
  p = len(order)  
  q = len(msg)//p
  return "".join([msg[i+q*j] for i in range (q) for j in order])

