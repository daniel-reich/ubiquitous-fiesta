
def esthetic(num):
    digits = '0123456789'
    x = num
    nums, bases = [], []
    base = 10
​
    while base > 1:
        rem = num % base
        nums.append(rem)
        num //= base
​
        if num == 0:
            res = []
            while nums:
                res.append(digits[nums.pop()])
​
            res = list(map(int, res))
​
            if all(abs(res[i] - res[i + 1]) == 1 for i, _ in enumerate(res[:-1])):
                bases.append(base)
                base -= 1
                num = x
            else:
                base -= 1
                num = x
​
    return sorted(bases) or 'Anti-Esthetic'

