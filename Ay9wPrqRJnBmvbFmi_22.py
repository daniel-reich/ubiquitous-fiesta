
def halve_count(num1, num2):
    count = -1
    while num1 > num2:
        num1 = num1/2
        count +=1
    return count

