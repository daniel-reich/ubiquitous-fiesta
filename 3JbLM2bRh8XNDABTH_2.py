
def basic_calculator(a, o, b):
    result = None
     
    if(o == "+"):
        result = a + b
    elif(o == "-"):
        result = a - b
    elif(o == "/" and b != 0):
        result = a / b
    elif(o == "*"):
        result = a * b
    return result

