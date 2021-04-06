
def stupid_addition(a, b):
​
    if type(a) != type(b) :
        return None
    elif type (a) and type(b) == str:
        return int(a) + int(b)
    elif type(a) and type(b) == int :
        return str(a) + str(b)

