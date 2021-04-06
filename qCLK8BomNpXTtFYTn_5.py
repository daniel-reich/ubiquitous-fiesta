
def cumulative_sum(lst):
    result = []
    for i in range(len(lst)):
        if i>0:
            result.append(result[-1]+ lst[i])
        else:
            result.append(lst[i])
    return result

