
import re
def solver(eq):
    left, right = eq.split(' =')
    lst_a_x = re.findall(r'\d+\*x(?= |$)', left)
    lst_c_x = re.findall(r'\d+\*x(?= |$)|(?<= )x(?= |$)', right)
    b = eval(left.replace('x', '0'))
    d = eval(right.replace('x', '0'))
    a = sum(int(i[:-2]) if len(i) > 1 else 1 for i in lst_a_x)
    c = sum(int(i[:-2]) if len(i) > 1 else 1 for i in lst_c_x)
    return 'Infinite solutions' if a - c == 0 else (d - b) / (a - c)

