
def will_hit(equation, position):
    if equation == "":
        return None
​
    igual_pos = equation.find('=')
    x_pos = equation.find('x')
​
    if(equation[igual_pos+1:x_pos].isspace()):
        m=1
        print(m)
    else:
        m = int(equation[igual_pos+1:x_pos])
        print(m)
​
    if(equation.find('+') == -1):
        b = int(equation[equation.rfind('-')+1:]) * -1
    else:
        b = int(equation[equation.find('+')+1:])
​
    x,y = position
​
    if(m*x + b == y):
        return True
    else:
        return False

