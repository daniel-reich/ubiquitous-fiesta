
def is_early_bird(_range, n):
    result_array = []
    str_n = str(n)
    len_n = len(str_n)
    string = ''.join((str(i) for i in range(_range+1)))
    count_n = string.count(str_n)
    tmp_indx = 0
    for x in range(len(string)-len_n+1):
        tmp_array = []
        if string[x:x+len_n] == str_n:
            for i in range(len(str_n)):
                tmp_array.append(x+i)
            result_array.append(tmp_array)
    if result_array[0][-1] < string.index(str(n-1)+str_n):
        result_array.append("Early Bird!")
    return result_array

