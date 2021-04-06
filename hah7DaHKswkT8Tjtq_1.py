
def separate_numbers(s):
    len_num = 1
    len_s = len(s)
    while len_num <= len_s // 2:
        s_tmp = s[:]
        start_num = s_tmp[:len_num]
        s_tmp = s_tmp[len_num:]
        next_num = int(start_num) + 1
        while s_tmp:
            str_next = str(next_num)
            if s_tmp.startswith(str_next):
                s_tmp = s_tmp[len(str_next):]
                next_num = int(str_next) + 1
            else:
                break
        if not s_tmp:
            return "YES {}".format(start_num)
        len_num += 1
    return "NO"

