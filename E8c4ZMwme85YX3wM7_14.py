
def recaman(n):
    if n == 0:
        return "---> Recaman's sequence: []\n---> Duplicates for n = 0: []"
    result = [0]*n
    result[0] = 0
    non_duplicate_result = []
    non_duplicate_result.append(0)
    duplicate = []
    for i in range(1, n):
        if result[i-1] > 0  and result[i-1] - i > 0 and result[i-1] - i not in result[:i]:
            result[i] = result[i-1] - i
        else:
            result[i] = result[i-1] + i
        if result[i] not in non_duplicate_result:
            non_duplicate_result.append(result[i])
        elif result[i] in non_duplicate_result:
            non_duplicate_result.append(-1)
    for i in range(len(result)):
        if non_duplicate_result[i] == -1:
            duplicate.append(result[i])
    final_duplicate = []
    for i in range(len(duplicate)):
        if duplicate[i] not in final_duplicate:
            final_duplicate.append(duplicate[i])
    return "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}".format(result, n, final_duplicate)

