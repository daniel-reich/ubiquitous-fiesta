
def is_factorial(n):
    if type(n) is tuple:
        if n[0]/n[1] == 1:
            return True;
        elif n[0]%n[1] == 0:
            return is_factorial((n[0]/n[1], n[1] + 1));
        else:
            return False;
    else:
        return is_factorial((n, 1));

