
def operation(a, b, op):
    d = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '//' }
    x = d.get(op)
    try: return str(eval(a+x+b))
    except: return 'undefined'

