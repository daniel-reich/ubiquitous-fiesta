
import re
def count_eatable_chocolates(txt, price):
    rx = re.compile(r'(?<!-)\b\d+(?=\s*(?:[$]|dollars))')
    m, p = rx.findall(txt), rx.findall(price)
    if not m or not p or p[0] == '0': return "Invalid Input"
    count = wrappers = int(m[0]) // int(p[0])
    while wrappers >= 3:
        chocs, wrappers = divmod(wrappers, 3)
        count += chocs
        wrappers += chocs
    return count

