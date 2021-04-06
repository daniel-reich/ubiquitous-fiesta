
def division(a, b):
    lst = []
    s = ""
    y = 1
​
    while y != 0:
        x, y = divmod(a, b)
        add = (x, y)
        
        if add not in lst:
            lst.append(add)
        else:
            start = (lst.index(add))
            start += len(str(lst[0][0])) - 1
            s = s[ : start] + "(" + s[start : ] + ")"
            break
        
        s += str(x)
        if x == 0:
            a *= 10
            if "." not in s:
                lst.append(".")
                s +="."
        if x > 0:
            a = 10 * y
            if "." not in s:
                lst.append(".")
                s +="."
    if s[-1] == ".":
        s += "0"
    return s

