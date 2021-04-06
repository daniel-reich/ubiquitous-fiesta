
import re
def dist(line, x, y):
    a = eval(re.findall(r'=(.+)x',line)[0])
    line = line.split('=')
    line = line[0] +"-("+ line[1] + ')'
    line = line.replace('x','*x')
    [x,y]=x,y
    return round(abs(eval(line))/(a**2 + 1**2)**0.5,2)

