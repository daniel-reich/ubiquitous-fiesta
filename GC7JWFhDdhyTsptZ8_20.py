
def sexy_primes(n, limit):
  primelst=[]
  
  result=[]
  for i in range (2,limit+1):
    for j in range (2,i):
      if i%j == 0: break
    else: primelst = primelst + [i]
  
  if n==2:
      for i in primelst:
        if i+6 in primelst: 
            result = result + [(i,i+6)]
  if n==3:         
     for i in primelst:
         if i+6 in primelst:
             if i+12 in primelst: 
                result = result + [(i,i+6,i+12)]
  return result

