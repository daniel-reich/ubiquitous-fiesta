
def operation(a, b, op):
    if op == "add": return str(int(a)+int(b))
    elif op == "subtract": return str(int(a)-int(b))
    elif op == "multiply" : return str(int(a)*int(b))
    elif b!="0" and op == "divide": return str(int(int(a)/int(b)))
    return "undefined"

