
def darts_solver(sections, darts, target):
    n_vars, length, res = darts, len(sections), set()
    for i in range(length ** n_vars):
        combination = []
        sum_darts = 0
        num = i
        for j in range(n_vars):
            combination.append(num % length)
            sum_darts += sections[num % length]
            num //= length
        if sum_darts == target:
            res.add(tuple(sorted(combination)))
    res = sorted(list(res))
    return ['-'.join(str(sections[i]) for i in tpl) for tpl in res]

