
def operation(a, b, o):
    if o == "add":
        return str(int(a) + int(b))
    elif o == "subtract":
        return str(int(a) - int(b))
    elif o == "multiply":
        return str(int(a) * int(b))
    elif o == "divide":
        if b == "0":
            return "undefined"
        else:
            return str(round(int(a) / int(b)))

