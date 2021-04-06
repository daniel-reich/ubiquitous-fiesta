
def nespers(lst):
​
    def count_sub_lists(x):
        return [len(x)] + [count_sub_lists(y)
                           for y in x if isinstance(y, list)]
​
    def factorial(n):
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod
​
    n_lists = eval('[' + str(count_sub_lists(lst))
                   .replace('[', '').replace(']', '') + ']')
    res = 1
    for k in n_lists:
        res *= factorial(k)
    return res

