
import re
​
def will_hit(equation, position):
    equation = equation.replace(" ", "")
    y, x, c, = re.search(r"([-+]*\d*y)=([-+]*\d*x)([+-]*\d*)", equation).group(1, 2, 3)
    ysub = "*" + str(position[1]) if bool(re.search(r'\d', y)) else str(position[1])
    xsub = "*" + str(position[0]) if bool(re.search(r'\d', x)) else str(position[0])
​
    y = y.replace('y', ysub)
    x = x.replace('x', xsub)
​
    return eval(y) == eval(x+c)

