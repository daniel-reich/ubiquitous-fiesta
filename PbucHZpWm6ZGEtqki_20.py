
def sliding_sum(lst, n, k):
    beg = 0
    end = beg + n
    ans = []
    while end <= len(lst):
        tot = sum([x for x in lst[beg:end]])
        if tot == k:
            ans.append(lst[beg:end])
        beg += 1
        end = beg + n
    return ans

