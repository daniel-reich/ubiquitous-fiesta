
def sum_two_smallest_nums(lst):
    positive_num = []
    [positive_num.append(x) for x in lst if x > 0]
    positive_num.sort()
    answer = positive_num[0] + positive_num[1]
    return answer

