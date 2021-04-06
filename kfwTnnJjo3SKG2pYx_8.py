
def replace_nums(string):
    num = ""
    ans = ""
    for c in string:
        if '0' <= c <= '9':
            num += c
        else:
            if num != "":
                ans += bin(int(num))[2:]
                num = ""
            ans += c
    if num != "":
        ans += bin(int(num))[2:]
    return ans

