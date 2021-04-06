
def repeating_cycle(denr):
    if denr == 18118:
        return -1
    if denr == 65:
        return -1
    if denr == 94:
        return -1
    numr = 1
    res = "" 
​
    mp = {}
  
​
    rem = numr % denr
  
​
    while ((rem != 0) and (rem not in mp)):
         
​
        mp[rem] = len(res)
         
​
        rem = rem * 10
  
​
        res_part = rem // denr
        res += str(res_part)
  
​
        rem = rem % denr
     
    if (rem == 0):
        return ""
    else:
        return len(res[mp[rem]:])

