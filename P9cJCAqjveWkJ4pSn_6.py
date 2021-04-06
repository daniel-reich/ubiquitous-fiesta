
def is_equal(num1, num2):
    if isinstance(num1,str) or isinstance(num2, str): 
        return False
    elif num1 != num2:
        return False
    else:
        return True

