
def shadow_sentence(a, b):
    x = a.split()
    y = b.split()
    if len(x) != len(y):                       return False
    for i in range(len(x)):
        if len(x[i]) != len(y[i]):             return False
        if len((set(x[i]) & set(y[i]))) > 0:   return False
    return True

