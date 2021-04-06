
def closing_in_sum(n):
    str_n = str(n)
    len_str_n = len(str_n)
    res = sum(int(str_n[i] + str_n[len_str_n - 1 - i])
              for i in range(len_str_n // 2))
    if len_str_n % 2:
        res += int(str_n[len_str_n // 2])
    return res

