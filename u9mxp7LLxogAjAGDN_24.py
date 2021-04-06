
def factor_sort(nums):
    factors = [(number,div(number)) for number in nums]
    return [i[0] for i in (sorted(factors,key = lambda x:(x[1],x[0]),reverse = True))]
def div(number):
    return len([i for i in range(1,number+1) if number % i == 0])

