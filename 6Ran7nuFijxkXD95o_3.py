
def keyboard_shortcut(txt):
    stack = []
    clipboard = []
    for i, x in enumerate(txt.split()):
        if x not in 'Ctrl+CV':
            stack.append(x)
        if x == 'C':
            clipboard = stack[:]
        if x == 'V' and clipboard:
            stack.extend(clipboard)
            clipboard = []
    return ' '.join(stack)

