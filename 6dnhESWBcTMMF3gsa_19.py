
def stupid_addition(a, b):
    if type(a)== type(b) == type(1):
        return str(a)+ str(b)
    elif type(a)==type(b) == type('a'):
        return int(a)+ int(b)
    else:
        return None

