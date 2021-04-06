
def single_GCD(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result
​
​
def GCD(lst):
    result_1 = single_GCD(min(lst))
    result_2 = single_GCD(min(lst))
    for ele in lst:
        for num in result_1:
            if ele % num != 0:
                result_2.remove(num)
        result_1 = result_2
    return max(result_1)

