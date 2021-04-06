
def meme_sum(a, b):
  a,b = str(a), str(b)              
  zero = "0"* abs(len(a)-len(b))    
  if len(a)>len(b):
    b = zero+b
  else:
    a = zero+a
    
  lst = [str(int(i)+int(j)) for i,j in zip(list(a),list(b))]
  return int("".join(lst))

