
def digital_division(n):
    p=1
    result = ""
    
    s = sum([int(x) for x in str(n)])
    for x in str(n):
        if int(x)!=0:
            p*=int(x)
​
    if (n%s==0):
        result+="1"
    
    if (n%p==0) and ('0' not in str(n)):
        result+="2"
    
    if all([ not(n%int(x)) for x in str(n) if int(x)!=0]):
        result+="0"
    
    if len(result)==0:
        return "Indivisible"
    elif len(result)==3:
        return "Perfect"
    else:
        return len(result)

