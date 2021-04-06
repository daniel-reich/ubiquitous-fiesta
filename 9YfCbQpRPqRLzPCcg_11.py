
def will_hit(equation, position):
    temp = equation.split(' ')
​
    m = int(temp[2][:-1])
    b = int(temp[4])
    if temp[3] == '-':
        b *= -1
​
    return m*position[0] + b == position[1]

