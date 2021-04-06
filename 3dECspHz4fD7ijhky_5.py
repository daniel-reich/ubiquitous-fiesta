
def numbers_range(ranges):
    ans = ""
    if len(ranges) == 0:
        return ans
    R = [ranges[0]]
    for cur in ranges[1:]:
        if cur == R[-1] + 1:
            R.append(cur)
        else:
            if len(R) >= 3:
                ans += ", " + str(R[0]) + "-" + str(R[-1])
            else:
                ans += ", " + ", ".join(map(str, R))
            R = [cur]
    if len(R) >= 3:
        ans += ", " + str(R[0]) + "-" + str(R[-1])
    else:
        ans += ", " + ", ".join(map(str, R))
    return ans[2:]

