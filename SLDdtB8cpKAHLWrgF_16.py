
def greater_permutation(expr, nums):
    permutations = [[0, 1, 2], [0, 2, 1],
                    [1, 0, 2], [1, 2, 0],
                    [2, 0, 1], [2, 1, 0]]
    res = []
    for p in permutations:
        tmp_expr = expr.replace('a', str(nums[p[0]])) \
            .replace('b', str(nums[p[1]])) \
            .replace('c', str(nums[p[2]]))
        eval_expr = eval(tmp_expr)
        if isinstance(eval_expr, float):
            eval_expr = round(eval_expr, 2)
            if abs(eval_expr - int(eval_expr)) < 0.01:
                eval_expr = int(eval_expr)
        res.append([eval_expr, tmp_expr + ' = ' + str(eval_expr)])
    res.sort()
    return res[-1][1]

