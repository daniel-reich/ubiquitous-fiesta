
def kaprekar_numbers(p, q):
    result = []
    for num in range(p, q+1):
        sqr_num = num ** 2
        num_right = int(str(sqr_num)[len(str(sqr_num)) - len(str(num)):])
        if len(str(sqr_num)) - len(str(num)) == 0:
            num_left = 0
        else:
            num_left = int(str(sqr_num)[:len(str(sqr_num)) - len(str(num))])
        if num_left + num_right == num:
            result.append(str(num))
    if result == []:
           return "INVALID RANGE"
    return " ".join(result)

