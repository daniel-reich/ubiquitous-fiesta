
def every_some(test, val, a, b, c, d, e):
        x = [a,b,c,d,e]
        y = 1 if isinstance(sum(x),int) or all([i for i in x])==bool else 0
        new = [eval(str(i)+test) for i in x if y == 1]
        return all(new) if val == 'everybody' else any(new)

