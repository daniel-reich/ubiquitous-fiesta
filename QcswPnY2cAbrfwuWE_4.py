
def filter_factorials(numbers):
    numbers2 = []
    f = []
    def factorial(num):
        if num == 1:
            return num
        return factorial(num - 1) * num
    for i in range(1,10):
        numbers2.append(factorial(i))
    for i in numbers:
        if i in numbers2:
            f.append(i)
    return f

