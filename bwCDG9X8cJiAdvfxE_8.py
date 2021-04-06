
def add_str_nums(num1, num2):
    if num1 =='' and num2=='':
        return '0'
    if num1=='':
        return num2
    if num2=='':
        return num1
    num1 = list(num1)
    num2 = list(num2)
    for i in num1:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            num1 = ''.join(num1)
        else:
            return '-1'     
    for i in num2:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            num2 = ''.join(num2)
        else:
            return '-1'  
        result = int(num1) + int(num2)
        return str(result)

