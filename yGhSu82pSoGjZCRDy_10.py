
def seesaw(num):
    if len(str(num))==1:
        return "balanced"
    elif num == None:
        return "balanced"
    else:
        raz = len(str(num))//2
        num1, num2 = int(str(num)[:raz]), int(str(num)[-raz:])
​
        if num1>num2:
            return "left"
        elif num2>num1:
            return 'right'
        else:
            return "balanced"

