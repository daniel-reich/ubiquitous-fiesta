
import re
​
def will_hit(equation, position):
​
    exp = r'([+-]?\d)x\s?([+-])?\s?(\d{1,})'
    cdr = re.compile(exp)
​
    gr = cdr.search(equation)
​
    m = int(gr.group(1))
​
    b = int(gr.group(2)+gr.group(3))
​
    if m*position[0]+b == position[1]:
        return True
    else:
        return False

