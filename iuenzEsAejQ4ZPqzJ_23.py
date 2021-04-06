
def mystery_func(num):
    test_num = 2
    remainder = 0
    num_of_twos = 1
    n = 1
    final_number = 0
    while True:
        if num - test_num < test_num:
            remainder = num - test_num
            break
        test_num *= 2
        num_of_twos += 1
    for i in range(num_of_twos):
        final_number += (2 * (10 ** (i + 1)))
    return final_number + remainder

