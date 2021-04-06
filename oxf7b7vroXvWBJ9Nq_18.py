
import re
​
def discount(n, txt):
    if not len(txt): return n
    discounts = sorted(txt.split(", "), key=lambda x: x[-1])
    for d in discounts:
        if d[-1] == "%":
            n -= float(d[:-1])/100*n
        else:
            n -= float(d)
    sol = "{:.2f}".format(n)
    return int(sol[:-3]) if sol[-3:] == ".00" else float(re.sub(r"0+$", "", sol))

