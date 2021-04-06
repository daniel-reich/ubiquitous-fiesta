
def staircase(k):
  
    staircase = []
    reverse = []
    x = 0
    symbol = "#"
    under = "_"
    
​
    if k >= 0:
        
        for x in range(k):
            
            string = ""
            for i in range(k-x):
                string += under
            for x in range(x):
                string += symbol
        
            x += 1
            
            if '#' in string:
                staircase.append(string)
​
        string2 = ""
        for x in range(k):
            string2 += symbol
        staircase.append(string2)
        
        for i in range(len(staircase)-1):
​
            staircase[i] += "\n"
    
        return ''.join(staircase)
    
    elif k < 0:
​
        k *= -1
​
        for x in range(k):
            
            string = ""
            for i in range(k-x):
                string += under
            for x in range(x):
                string += symbol
        
            x += 1
            
            if '#' in string:
                staircase.append(string)
​
        string2 = ""
        for x in range(k):
            string2 += symbol
        staircase.append(string2)
    
    
        for item in staircase:
        
            index = staircase.index(item)
            index += 1 
            index *= -1
            reverse.append(staircase[index])
        
        for i in range(len(reverse)-1):
​
            reverse[i] += "\n"
        
        return ''.join(reverse)

