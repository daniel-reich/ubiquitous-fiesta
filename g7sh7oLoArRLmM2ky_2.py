
def baconify(msg, *mask):
  if not mask:   #decyphering
    bins = [l.islower() for l in msg if l.isalpha()]
    ords = [97+bin_to_int(bins[5*i:5*i+5]) for i in range(0,(1+len(bins))//5)]
    
    return "".join(' ' if o==128 else '.' if o==127 else chr(o) for o in ords)
    
  #encrypting
  caps = sum((sym_to_bin(l) for l in msg if l not in "'!?'"),[])
  ans = ""
  for x in mask[0]:
    if caps and x.isalpha():
      i = caps.pop(0)
      ans+= x.lower() if i else x.upper()
    else: ans+= x.lower()
    
  return ans
    
bin_to_int = lambda lst: sum(2**(len(lst)-1-k)*lst[k] for k in range(len(lst)))
​
def sym_to_bin(sym):
  if sym == " ": return [1,1,1,1,1]
  if sym == ".": return [1,1,1,1,0]
  return [((ord(sym.lower())-97)//(2**k))%2 for k in range(5)][::-1]

