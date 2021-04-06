
def add_str_nums (num1, num2):
    num1, num2 = num1.lstrip ("0"), num2.lstrip ("0")
    num1 = "0" if num1 == "" else num1
    num2 = "0" if num2 == "" else num2
    if not num1.isnumeric() or not num2.isnumeric():
        return "-1"
    if len(num1) <= len(num2):
        lower, greater = num1, num2
    else:
        lower, greater = num2, num1
    lower = "0" * (len(greater) - len(lower)) + lower
    res, carry = "", 0
    for i in range(1, len(greater)+1):
        add = str(int(greater[-(i)]) + int(lower[-(i)]) + carry)
        if len(add) > 1:
            add = add[1:]
            carry = 1
        else:
            carry = 0
        res = add + res
    if carry == 1:
        res = "1" + res
    return res

