
def will_fit(holds, cargo):
    d={
       "S" : 50,
       "M" : 100, 
       "L" : 200 
      }
    fit=True
    for h,c in zip(holds,cargo):
        if d[h]<c:
            return False
    
    return fit

