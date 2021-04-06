
def every_some(test, val, *a):
    return all(eval(str(x) + test) for x in a) if val == 'everybody' else any(eval(str(x) + test) for x in a)

