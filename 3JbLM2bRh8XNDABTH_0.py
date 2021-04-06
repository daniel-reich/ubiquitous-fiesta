
def basic_calculator(a, o, b):
    if (o=="/" and b!=0) or o in "+-*":
        return eval(str(a) + o + str(b))

