
def max_possible(num, digits):
    num_list = [int(x) for x in str(num)]
    digits_list = [int(x) for x in str(digits)]
    digits_list.sort()
    digits_list = digits_list[::-1]
    for n in range(0,len(num_list)):
        if len(digits_list) > 0 and num_list[n] < digits_list[0]:
            num_list[n] = digits_list.pop(0)
    num_list = [str(x) for x in num_list]
    return int("".join(num_list))

