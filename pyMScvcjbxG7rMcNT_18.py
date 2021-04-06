
def sum_list(nums):
    out = 0
    for num in nums:
        if type(num) == list:
            for n in num:
                if type(n) == list:
                    for i in n:
                        out += i
                else:
                    out += n
        else:
            out += num
    return out

