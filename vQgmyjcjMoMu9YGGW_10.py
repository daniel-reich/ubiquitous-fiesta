
def simplify(txt):
    spl_txt = txt.split('/')
    first_num = int(spl_txt[0])
    second_num = int(spl_txt[1])
    if (first_num / second_num) % 1 == 0:
        return str(int(first_num / second_num))
    lower_num = min(first_num, second_num)
    for i in range(0, lower_num):
        if first_num % (lower_num - i) == 0 and second_num % (lower_num - i) == 0:
            return str(int(first_num / (lower_num - i))) + '/' + str(int(second_num / (lower_num - i)))

