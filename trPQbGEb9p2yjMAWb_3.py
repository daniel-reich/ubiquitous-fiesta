
def evaluate(test, value):
    return eval(str(value) + test)
​
#def every_some(test, val, a, b, c, d, e):
def every_some(test, val, *lst):
    results = [evaluate(test, value) for value in lst]
    return all(results) if val == "everybody" else any(results)

