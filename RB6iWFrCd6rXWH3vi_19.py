
def longest_substring(nums: str) -> str:
    temp_max, temp = '', ''
    for i, v in enumerate(nums):
        if temp == '':
            temp += v
        elif int(temp[-1]) % 2 != int(v) % 2:
            temp += v
        else:
            if len(temp) > len(temp_max):
                temp_max = temp
            temp = v
    if len(temp) > len(temp_max):
        temp_max = temp
    return temp_max

