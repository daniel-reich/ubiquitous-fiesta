
import re
​
​
def solve(eq):
    pattern = re.compile(r'.\d+')
    num1 = pattern.findall(eq)
    signal = eq[2]
    if signal == '+':
        return int(num1[1]) - int(num1[0])
    else:
        return int(num1[1]) + int(num1[0])

