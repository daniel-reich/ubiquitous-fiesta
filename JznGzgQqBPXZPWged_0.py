
import re
​
def ohms(s):
    res = 1/sum(1/i for i in eval(s)) if s[0] == '[' else sum(eval(s))
    return str(res)
​
def resist(net):
    while '(' in net or '[' in net:
        net = re.sub(r'[\[\(][\d,. ]+[\)\]]', lambda x: ohms(x.group()), net)
    return round(float(net), 1)

