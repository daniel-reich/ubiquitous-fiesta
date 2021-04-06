
def post_fix(expression):
    '''
    Returns the evaluation of expression, which is (sort of!) in post fix notation
    '''
    expression = expression.split()
    operands = [item for item in expression if item.isnumeric()]
    operators = [item for item in expression if item in '+-*/']
    expr = ''.join([operands[i]+op for i, op in enumerate(operators)]+[operands[-1]]) 
    
    return eval(expr)

