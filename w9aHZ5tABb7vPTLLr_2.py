
def lucky_ticket(n_digits):
    if n_digits == 2:
        return 10
​
    half = n_digits // 2
    max_sum = 9 * half
    sums = dict()
    for s in range(max_sum + 1):
        sums[s] = 0
​
    str_tpl = ''
    str_loop = ''
    for i in range(half):
        str_tpl += 'd{}, '.format(i)
        str_loop += ' for d{} in range(10)'.format(i)
    eval_expr = '(({}){})'.format(str_tpl[:-2], str_loop)
​
    gen = eval(eval_expr)
    for tpl in gen:
        sums[sum(tpl)] += 1
​
    return sum(val * val for val in sums.values())

