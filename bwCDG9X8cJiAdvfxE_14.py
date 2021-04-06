
def add_str_nums(num1, num2):
    if num1 == "":
        num1 = "0"
    if num2 == "":
        num2 = "0"
    if num1.isnumeric() and num2.isnumeric():
        return str(int(num1) + int(num2))
    else:
        return "-1"

