
def postfix(expression):
    operators, stack = '+-*/', []
    for item in expression.split():
        if item not in operators:
            stack.append(item)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(str(eval(operand_2 + item + operand_1)))
    return int(float(stack.pop()))

