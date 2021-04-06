
def palindrome_descendant(num):
    str_num = str(num)
    while len(str_num) > 1:
        if str_num == str_num[::-1]:
            return True
        str_new_num = ''
        for i in range(0, len(str_num), 2):
            sum_pair = int(str_num[i]) + int(str_num[i + 1])
            str_new_num += str(sum_pair)
        if len(str_new_num) % 2:
            return False
        str_num = str_new_num
    return False

