
def create_square(l):
    if l == None or l < 1:
        return ''
    elif l == 1:
        return '#'
    else:
        return '#'*l + '\n' + ('#'+' '*(l-2) + '#\n')*(l-2) + '#'*l

