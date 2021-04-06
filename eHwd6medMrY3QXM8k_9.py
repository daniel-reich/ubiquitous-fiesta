
def is_consecutive(s):
  return any([all([num - decoupe(s,p)[i+1] == 1 for i, num in enumerate(decoupe(s,p)[:-1])]) or 
        all([num - decoupe(s,p)[i+1] == -1 for i, num in enumerate(decoupe(s,p)[:-1])])
         for p in range(1,len(s)//2+1)])
​
def decoupe(string,p):
  if len(string)%p == 0:
    return [int(string[p*i:p*(i+1)]) for i in range(len(string)//p)]
  else:
    return [1,3]

