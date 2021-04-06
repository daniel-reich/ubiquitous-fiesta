
import math
​
def hex_lattice(n):
    x = 3 + math.sqrt((12*n) - 3)
    x /= 6
​
    if math.ceil(x) == math.floor(x):
        maxw = int(4*x - 1)
​
        hexagon = []
​
        for y in range(int(x), int(2*x)):
            b = int(((maxw-(2*y-1))/2))
            hexagon += [" "]*b
            for z in range(y):
                hexagon += ["o"]
                if not z == y-1:
                    hexagon += [" "]
            hexagon += [" "]*b
            hexagon += "\n"
​
        for y in reversed(range(int(x), int(2*x-1))):
            b = int(((maxw-(2*y-1))/2))
            hexagon += [" "]*b
            for z in range(y):
                hexagon += ["o"]
                if not z == y-1:
                    hexagon += [" "]
            hexagon += [" "]*b
            hexagon += "\n"
​
        hexagon = "".join(hexagon [:-1])
​
        return hexagon
    else:
        return "Invalid"

