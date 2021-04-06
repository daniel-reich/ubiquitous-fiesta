
def basic_calculator(a, o, b):
    ops =  ["*","/","+","-"]
    ws = "/0"
    s = str(a) + o + str(b) 
    if o in ops and ws not in s:
        return eval(s)
    else:
        return None

