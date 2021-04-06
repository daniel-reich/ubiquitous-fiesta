
def catch_zero_division(n):
    try:
        eval(n)
    except ZeroDivisionError :
       return True
    return False

