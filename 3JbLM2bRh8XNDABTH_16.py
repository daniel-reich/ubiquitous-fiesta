
def basic_calculator(a,o,b):
    if o == '+' :
        c = a + b
    elif o == '-' :
        c = a - b
    elif o == '/' :
        if b == 0:
            return None
        c = a / b
    elif o == '*' :
        c = a * b
    else:
        c = print("None",o, "is not an operator")
    return c

