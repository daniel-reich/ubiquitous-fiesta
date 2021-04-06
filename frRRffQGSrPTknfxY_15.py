
def digit_count(n):
    split_lst = [val for val in str(n)]
    result = str(n)
    f_result = ""
    for i in split_lst:
        f_result += str(split_lst.count(i))
    return int(f_result)

