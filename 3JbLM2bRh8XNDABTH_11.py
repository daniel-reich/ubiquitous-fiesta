
def basic_calculator(a, o, b):
    result = 0
     
    if(o == "+"):
        return a + b
    if(o == "-"):
        return a - b
    if (o == "/" and b != 0):
        return a / b
    if(o == "*"):
        return a * b

