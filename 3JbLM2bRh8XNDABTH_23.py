
def basic_calculator(a, o, b):
    result = 0
     
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == '/' and a != 0 and b != 0:
        return a / b
    elif o == "*":
        return a * b

