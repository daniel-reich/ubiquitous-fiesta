
def multiply_by_11(s, ans="", cnt=11):
    if cnt == 0:
        return ans
    if ans == "":
        return multiply_by_11(s, s, 10)
    s2 = s.zfill(len(ans))
    carry = 0
    new_ans = ""
    for i in range(len(ans) - 1, -1, -1):
        a = int(ans[i]) + int(s2[i]) + carry
        new_ans = str(a % 10) + new_ans
        carry = a // 10
    if carry > 0:
        new_ans = '1' + new_ans
    return multiply_by_11(s, new_ans, cnt - 1)

