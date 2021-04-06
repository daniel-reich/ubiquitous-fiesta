
def mathematical_function(mathfunc, numbers):
    f, exp = mathfunc.split("=")
    exp = exp.replace("x", "*").replace("^", "**").replace("/", "//")
    return ["{}={}".format(f.replace("y", str(n)), eval(exp.replace("y", str(n)))) for n in numbers]

