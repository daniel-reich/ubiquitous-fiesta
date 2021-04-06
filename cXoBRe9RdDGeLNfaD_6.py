
def eight_bit(exp):
    num_one, operator, num_two = exp.split(" ")
    num_one, num_two = int(num_one), int(num_two)
    if num_one < -128 or num_one > 127 or num_two < -128 or num_two > 127:
        return "Overflow"
    result = eval("{}{}{}".format(num_one, operator, num_two))
    if result > 127 or result < -128:
        return "Overflow"
    return (result, "{} {} {} = {}".format(bin(num_one)[2:] if num_one > 0 else bin(num_one & 255)[2:], operator, bin(num_two)[2:] if num_two > 0 else bin(num_two & 255)[2:], bin(result & 255)[2:]))

