
def factor_sort(nums):
    dic = {key : 0 for key in nums}
    for number in nums:
        dic[number] = len([d for d in range(1, number + 1) if number % d == 0])
    return [i[0] for i in sorted(dic.items(), key=lambda p : (p[1], p[0]), reverse=True)]

