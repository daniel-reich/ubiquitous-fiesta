
def basic_calculator(a, o, b):
    result = 0
     
    if(o == "+"): 
        result = a + b
    elif(o == "-"): 
        result = a - b
    elif(o == "/" and b != 0): 
        result = a / b
    elif(o == "*"): 
        result = a * b
    else:
        result = None
​
    return result

