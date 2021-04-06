
def multiply_by_11(n):
    n = '0' + n
    ans = n[-1]
    carry = 0
    for pos in range(len(n)-2, -1, -1):
        box = n[pos:pos+2]
        s = int(box[0]) + int(box[1]) + carry
        ans = str(s % 10) + ans
        carry = s // 10
    if carry > 0:
        ans = str(carry) + ans
    return ans

