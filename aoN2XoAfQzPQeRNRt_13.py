
def operation(a, b, op):
    d = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '//'}
    try:
        return str(eval('{}{}{}'.format(a, d[op], b)))
    except ZeroDivisionError:
        return 'undefined'

