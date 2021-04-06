
def simplify(txt):
    lis = txt.split("/")
    num1 = int(lis[0])
    num2 = int(lis[1])
    if not num1 % num2:
        return "{}".format(num1//num2)
    factors_of_num1 = [x for x in range(1, num1+1) if not num1 % x]
    factors_of_num2 = [y for y in range(1, num2+1) if not num2 % y]
    highest_common_factor = max(
        [a for a in factors_of_num1 if a in factors_of_num2])
    return "{}/{}".format(num1//highest_common_factor, num2//highest_common_factor)

