
def true_equations(lst):
    output = []
    for i in lst:
        if eval(i.split("=")[0])==eval(i.split("=")[1]):
            output.append(i)
    return output

