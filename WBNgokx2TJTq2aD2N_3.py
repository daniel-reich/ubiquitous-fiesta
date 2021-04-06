
def smallest(d, v):
  
    x = int("1" + "0" * (d-1))
    while x>1:
        if x%v==0:
            return(x)
            break
        else:
            x+=1

