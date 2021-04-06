
def reversible_inclusive_list(start, end, ans=[]):
    if ans == []:
        ans = [start]
    else:
        ans.append(start)
    if start == end:
        return ans
    elif start < end:
        return reversible_inclusive_list(start + 1, end, ans)
    else:
        return reversible_inclusive_list(start - 1, end, ans)

