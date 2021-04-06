
def split(n):
    result_list = []
    for i in range(1, n+1):
        split_num = n/i
        temp = round(split_num**i,1)
        result_list.append(temp)
    return max(result_list)

