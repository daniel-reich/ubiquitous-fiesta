
def mathematical(exp, numbers):
    
    a = list(exp)[5:]
    
    result = []
    
    if a[1] == "^":
        for i in numbers:
            result.append("f({})={}".format(i,i**int(a[2])))
        
    elif a[1] == "x":
        for i in numbers:
            result.append("f({})={}".format(i,i*int(a[2])))
    
    elif a[1] == "+":
        for i in numbers:
            result.append("f({})={}".format(i,i+int(a[2])))    
    
    elif a[1] == "-":
        for i in numbers:
            result.append("f({})={}".format(i,i-int(a[2])))
    
    elif a[1] == "/":
        for i in numbers:
            result.append("f({})={}".format(i,i//int(a[2])))
            
            
    
    return result

