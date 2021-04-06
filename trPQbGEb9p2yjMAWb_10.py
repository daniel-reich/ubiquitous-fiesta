
def every_some(test, val, a, b, c, d, e):
    return all(eval(str(i) + test) for i in (a, b, c, d, e)) if val == "everybody" else any(eval(str(i) + test) for i in (a, b, c, d, e))

