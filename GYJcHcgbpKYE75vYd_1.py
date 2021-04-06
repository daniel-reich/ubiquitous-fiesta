
suffix = {'1': '-ST', '2': '-ND', '3': '-RD'}
def return_end_of_number(num):
    str_num = str(num)
    if len(str_num) > 1 and str_num[-2] == '1' or str_num[-1] not in suffix:
        return '{}-TH'.format(str_num)
    return '{}{}'.format(str_num, suffix[str_num[-1]])

