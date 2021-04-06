
def keys_and_values(d):
  
    keys = []
    val = []
    
    ans = []
    
    for k in d:
        keys.append(k)
        keys = sorted(keys)
        
    for i in range(len(keys)):
        val.append(d.get(keys[i]))
        
    ans.append(keys)
    ans.append(val)
    
    return ans

