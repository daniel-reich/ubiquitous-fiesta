
def prefix(exp):
    ops = {'+', '-', '*', '//'}
    stack = []
    exp = exp.replace('/', '//').split()
    for i in exp:
        if i in ops:
            stack.append(i)
        else:
            if not stack[-1] in ops:
                stack.append(str(eval('{}{}{}'.format(stack.pop(), stack.pop(), i))))
            else:
                stack.append(i)
    if len(stack) == 1:
        return int(stack[0])
    return int(str(eval('{}{}{}'.format(stack[1], stack[0], stack[2]))))

