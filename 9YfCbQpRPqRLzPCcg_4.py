
def will_hit(equation, position):
    equation = equation.split(" ")
    right_side = 0
    left_side = position[-1]
    slope = int(equation[2][0:-1]) * position[0]
    if equation[-2] == "-":
        right_side = slope - int(equation[-1])
    elif equation[-2] == "+":
        right_side = slope + int(equation[-1])
    else:
        return
    if left_side == right_side:
        return True
    else:
        return False

