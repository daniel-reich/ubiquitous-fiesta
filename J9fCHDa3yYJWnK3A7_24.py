
def is_happy(n):
​
    temp = 0
    for i in range(len(str(n))):
        temp = temp + int(str(n)[i]) ** 2
​
    if temp == 1:
        return True
    elif temp == 4:
        return False
    else:
        return is_happy(temp)

