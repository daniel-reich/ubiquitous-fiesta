
def add_str_nums(num1, num2):
    if not num1:
        num1 = 0
    if not num2:
        num2 = 0
    try:
        return str(int(num1) + int(num2))
    except ValueError:
        return '-1'

