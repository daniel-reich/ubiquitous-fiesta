
def accumulate(nums):
    accumulate = []
    total = 0
    for i in nums:
        total += i
        accumulate.append(total)
    return accumulate
​
​
def break_point(num):
    lst = [int(i) for i in ' '.join(str(num)).split()]
    x = accumulate(lst)
    y = list(reversed(accumulate(reversed(lst))))
    guess = []
    for index, i in enumerate(x):
        if i >= y[index + 1]:
            if i == y[index + 1]:
                return True
            return False

