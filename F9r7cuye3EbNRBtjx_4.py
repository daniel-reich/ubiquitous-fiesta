
def string_builder(s): 
    airforce = []
    fan = [] 
    t = ""
    r = ""  
    i = 0
    while i < len(s): 
      count = 0
      if (s[i] >= '0' and s[i] <='9'): 
        while (s[i] >= '0' and s[i] <= '9'): 
          count = count * 10 + ord(s[i]) - ord('0')  
          i += 1
        i -= 1
        airforce.append(count) 
      elif (s[i] == ']'): 
        t = ""  
        count = 0
        if (len(airforce) != 0): 
          count = airforce[-1]  
          airforce.pop() 
        while (len(fan) != 0 and fan[-1] !='[' ): 
          t = fan[-1] + t  
          fan.pop() 
        if (len(fan) != 0 and fan[-1] == '['):  
          fan.pop()  
        for j in range(count): 
          r = r + t  
        for j in range(len(r)): 
          fan.append(r[j])  
        r = "" 
      elif (s[i] == '['): 
        if (s[i-1] >= '0' and s[i-1] <= '9'):  
          fan.append(s[i])
        else: 
          fan.append(s[i])  
          airforce.append(1) 
      else: 
        fan.append(s[i]) 
      i += 1
    while len(fan) != 0: 
      r = fan[-1] + r  
      fan.pop()
    return r

