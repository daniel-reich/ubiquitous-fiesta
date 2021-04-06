
def permutation(cur, list_to_permutation, used_indexes, result_of_permutation):
    if len(cur) == len(list_to_permutation):
        result_of_permutation.append(cur[:])
    for i in range(len(list_to_permutation)):
        if i in used_indexes:
            continue
        cur.append(list_to_permutation[i])
        used_indexes.append(i)
        permutation(cur, list_to_permutation, used_indexes, result_of_permutation)
        cur.pop()
        used_indexes.pop()
    return result_of_permutation
    
def greater_permutation(expr, nums):
    result_of_permutation_of_nums = permutation([], nums, [], [])
    max_value = eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                    str(result_of_permutation_of_nums[0][2])))
    if int(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b", str(
            result_of_permutation_of_nums[0][1]))). \
                        replace("c", str(result_of_permutation_of_nums[0][2])))) == eval(((
                        expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace("b",
                                                                         str(result_of_permutation_of_nums[0][1]))). \
                                                                                                 replace("c", str(result_of_permutation_of_nums[0][2]))):
            final_result = ((expr.replace("a", str(result_of_permutation_of_nums[0][0]))) \
                        .replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", str(
                        result_of_permutation_of_nums[0][2])) \
                       + " = " + str(int(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace(
                       "b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                                                    str(result_of_permutation_of_nums[0][2])))))
​
​
    else:
        final_result = ((expr.replace("a", str(result_of_permutation_of_nums[0][0]))) \
                        .replace("b", str(result_of_permutation_of_nums[0][1]))).replace("c", str(
            result_of_permutation_of_nums[0][2])) \
                       + " = " + str(
            round(float(eval(((expr.replace("a", str(result_of_permutation_of_nums[0][0]))).replace(
                "b", str(result_of_permutation_of_nums[0][1]))).replace("c", \
                                                                        str(result_of_permutation_of_nums[0][2])))), 2))
​
    for i in range(1, len(result_of_permutation_of_nums)):
        if max_value < eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2]))):
            max_value = eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2])))
            if int(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace("b", str(result_of_permutation_of_nums[i][1]))).\
                                replace("c", str(result_of_permutation_of_nums[i][2])))) == eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace("b", str(result_of_permutation_of_nums[i][1]))).\
                                replace("c", str(result_of_permutation_of_nums[i][2]))):
                      final_result = ((expr.replace("a", str(result_of_permutation_of_nums[i][0])))\
                                         .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(result_of_permutation_of_nums[i][2])) \
                           + " = " + str(int(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace(
                                        "b", str(result_of_permutation_of_nums[i][1]))).replace("c", \
                                                                        str(result_of_permutation_of_nums[i][2])))))
​
​
            else:
                final_result = ((expr.replace("a", str(result_of_permutation_of_nums[i][0]))) \
                                .replace("b", str(result_of_permutation_of_nums[i][1]))).replace("c", str(
                    result_of_permutation_of_nums[i][2])) \
                               + " = " + str(round(float(eval(((expr.replace("a", str(result_of_permutation_of_nums[i][0]))).replace(
                    "b", str(result_of_permutation_of_nums[i][1]))).replace("c", \
                                                                            str(result_of_permutation_of_nums[i][2])))), 2))
​
    return final_result

