
def license_plate(s, n):
    s = s.replace('-','')
    s = s.upper()
    reminder = len(s)%n
    output=""
    
    for x in range(len(s)):
            
        if(x%n==0 and x!=0  and reminder == 0): 
            output=output+"-"
        elif(reminder !=0 and (x == reminder or (x-reminder)%n==0)):
            output=output+"-"
        print(reminder)
        
        output=output+s[x]
  
            
    return output

