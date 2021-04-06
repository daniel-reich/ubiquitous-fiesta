
def solve(exp):
    if "+" in exp:
        return str(int(exp.split("+")[0]) + int(exp.split("+")[1]))
    elif "-" in exp:
        return str(int(exp.split("-")[0]) - int(exp.split("-")[1]))
    elif "/" in exp:
        return str(int(int(exp.split("/")[0]) / int(exp.split("/")[1])))
    elif "x" in exp:
        return str(int(exp.split("x")[0]) * int(exp.split("x")[1]))
    else:
        return str(int(exp.split("^")[0]) * int(exp.split("^")[0]))        
def mathematical(exp, numbers):
    outputarr = [exp.split("=")[0].replace("y", str(number)) + "=" + solve(exp.split("=")[1].replace("y", str(number))) for number in numbers]
    return outputarr

