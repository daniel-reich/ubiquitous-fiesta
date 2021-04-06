
def operation(a, b, op):
    dct = {'add': lambda x, y: x + y, 'subtract': lambda x, y: x - y,
        'divide': lambda x, y: x // y, 'multiply': lambda x, y: x * y}
    try:
        return str(dct[op](int(a), int(b))) 
    except ZeroDivisionError as er:
        return 'undefined'

