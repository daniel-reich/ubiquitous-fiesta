
def will_hit(equation, position):
​
    if '-' in equation[3:6]:
        m = int(equation[4:6])
        b = int(equation[8]+equation[10:])
    elif equation[3] == '' :
        m = 1
        b = int(equation[6]+equation[8])
    elif equation[4] == '-':
        m = -1
        b = int(equation[7]+equation[9])
    else:
        m = int(equation[3:5])
        b = int(equation[7]+equation[9])
​
    return position[1] == (m*position[0])+b

