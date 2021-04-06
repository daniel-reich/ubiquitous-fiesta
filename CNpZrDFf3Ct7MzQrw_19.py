
def trouble(num1, num2):
    i = 0
    j = 0
    occurenceNum1 = 1
    occurenceNum2 = 1
    num1 = str(num1)
    num2 = str(num2)
    while occurenceNum1 != 3 and i < len(num1)-1:
        if num1[i] == num1[i+1]:
            occurenceNum1 += 1
            i+=1
        else:
            i+=1
​
    while occurenceNum2 != 2 and j < len(num2)-1:
        if num2[j] == num2[j+1]:
            occurenceNum2 += 1
            j+=1
        else:
            j+=1
​
    if occurenceNum1 == 3 and occurenceNum2 == 2:
        return True
    else:
        return False

