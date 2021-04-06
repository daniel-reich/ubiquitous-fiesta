
def inclusive_list(start_num, end_num):
    result = []
    if start_num < end_num:
        for i in range(start_num, end_num+1):
            result.append(i)
    else:
        result.append(start_num)
    return result

