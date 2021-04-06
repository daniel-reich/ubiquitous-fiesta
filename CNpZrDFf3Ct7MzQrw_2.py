
def trouble(num1, num2):
    (num1,num2) = (str(num1),str(num2))
    for i in num2:
        if i*2 in num2 and i*3 in num1:
            return True
    return False

