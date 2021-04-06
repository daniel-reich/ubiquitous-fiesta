
def add_str_nums(num1, num2):
    try:
        return str(int(num1) + int(num2))
    except:
        if num1 == '' and num2 == '':
            return '0'
        elif num1 == '' or num2 == '':
            return num1 + num2
        elif not num1.isdigit() or not num2.isdigit():
            return '-1'

