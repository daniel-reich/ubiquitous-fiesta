
def prefix(exp):
    stack = []
    for element in exp.split()[::-1]:
        if not element in '+-*/':
            stack.append(int(element))
        else:
            stack.append(eval("{} {} {}".format(stack.pop(), element, stack.pop())))
    return int(stack.pop())

