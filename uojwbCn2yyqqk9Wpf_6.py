
n_max = 3600
sum_divisors = [0, 0] + [sum(i for i in range(1, k // 2 + 1) if not k % i)
                         for k in range(2, n_max + 1)]
def is_untouchable(num):
    if num < 2:
        return 'Invalid Input'
    res = [i for i in range(num, n_max + 1)
           if sum_divisors[i] == num]
    return res if res else True

