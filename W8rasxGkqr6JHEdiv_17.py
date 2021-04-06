
def permutation_operators_backtracking(cur, lst_operators, result, k):
    if len(cur) == k:
        result.append(cur[:])
    if len(cur) > k:
        return
    else:
        for i in range(len(lst_operators)):
            cur.append(lst_operators[i])
            permutation_operators_backtracking(cur, lst_operators, result, k)
            cur.pop()
    return result
​
​
​
def permutation_operands(cur, lst_operands, used_indexes, result):
    if len(cur) == len(lst_operands):
        result.append(cur[:])
    for i in range(len(lst_operands)):
        if i in used_indexes:
            continue
        cur.append(lst_operands[i])
        used_indexes.append(i)
        permutation_operands(cur, lst_operands, used_indexes, result)
        cur.pop()
        used_indexes.pop()
    return result
​
def string_join(lst_1, str_2):
    result = []
    for i in range(len(str_2)):
        result.append(str(lst_1[i]))
        result.append(str_2[i])
    result.append(str(lst_1[-1]))
    return ''.join(result)
​
​
​
​
def countdown(operands, target):
    lst_operands = permutation_operands([], list(operands), [], [])
    lst_operators = permutation_operators_backtracking([], ["+", "-", "*", "//"], [], len(operands) - 1)
    for item in lst_operands:
        for combo in lst_operators:
            result = string_join(item, combo)
            if eval(result) == target:
                return result
    return None

