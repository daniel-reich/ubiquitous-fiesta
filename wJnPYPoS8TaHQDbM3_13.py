
def convert10_to_base(n, base):
    result, extra_digits = '', 'ABCDEF'
    while n > 0:
        remainder = n % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += extra_digits[remainder - 10]
        n = n // base
    return result[::-1]
​
​
def make_dices_combination(num, n_digits):
    res = n_digits * [1]
    s = convert10_to_base(num, 6)
    for j in range(1, min(len(s), len(res)) + 1):
        res[-j] += int(s[-j])
    return res
​
​
def dice_roll(n, outcome):
    count = 0
    for i in range(6 ** n):
        if sum(make_dices_combination(i, n)) == outcome:
            count += 1
    return count

