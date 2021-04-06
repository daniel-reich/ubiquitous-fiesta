
def catch_zero_division(expr):
    try:
        eval(expr)
    except ZeroDivisionError:
        return True
    return False

