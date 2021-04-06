
def print_all_groups():
    lets = "abcde"
    nums = "123456"
    s = ""
    for n in nums:
        for l in lets:
            s += n + l + ", "
    return s[:-2]

