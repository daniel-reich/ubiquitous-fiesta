
import math
​
def triangle(perimeter,area):
    ans = []
    for a in range(1, perimeter - 1):
        for b in range(1, perimeter - 1):
            c = perimeter - a - b
            sides = sorted([a, b, c])
            if a + b <= c or a + c <= b or b + c <= a:
                continue
            s = (a + b + c) / 2.
            A = math.sqrt(s * (s - a) * (s - b) * (s - c))
            if abs(A - area) < 1e-5 and sides not in ans:
                ans.append(sides)
    return ans

