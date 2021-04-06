
def break_point(num):
    num_str = str(num)
    for i in range(len(num_str)):
        lst1 = list(num_str[0:i])
        lst2 = list(num_str[i::])
        num1 = 0
        for j in range(len(lst1)):
            num1 += int(lst1[j])
        
        num2=0
        for j in range(len(lst2)):
            num2 += int(lst2[j])
        if num1 == num2:
            return True
    return False

