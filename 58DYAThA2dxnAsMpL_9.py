
def integer_boolean(n):
    s = str(n)
    b= []
    for i in s:
        if i=="1":
            b.append(True)  
        elif i== "0":
            b.append(False)    
    return b

