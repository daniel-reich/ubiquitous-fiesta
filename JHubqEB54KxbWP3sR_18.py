
import math
​
​
def dist(line, x, y):
    index_x = line.find("x")
    if line[2] != "(":
        num_a = eval(line[2:index_x])
    elif line[2] == "(":
        num_a = eval(line[3:index_x-1])
    num_b = eval(line[index_x + 1:])
    line = line[:index_x] + "*" + line[index_x:]
    line = line[2:] + "-y"
    line = line.replace("x", str(x))
    line = line.replace("y", str(y))
    return round(abs(eval(line)) / math.sqrt(num_a ** 2 + 1), 2)

