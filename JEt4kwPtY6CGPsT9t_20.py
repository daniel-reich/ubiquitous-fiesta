
def mathematical(exp, numbers):
    for rep in (("/","//"),("x","*"),("^","**")):    
        exp=exp.replace(*rep)
    return ["f("+str(y)+")="+str(eval(exp.split("=")[1])) for y in numbers]

