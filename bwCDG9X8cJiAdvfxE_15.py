
def add_str_nums(num1, num2):
    if num1 == "" and num2 == "":
        return "0"
    elif num1 == "":
        return num2
    elif num2 == "":
        return num1
    else:
        try:
            return str(int(num1) + int(num2))
        except:
            return "-1"

