
def combinator2(lst, delim, ans):
    if lst == []:
        return ans
    new_ans = []
    for a in ans:
        for b in lst[0]:
            new_ans.append(a + delim + b)
    return combinator2(lst[1:], delim, new_ans)
​
def combinator(lst, delim=''):
    if len(lst) == 0:
        return ans
    ans = lst[0]
    return combinator2(lst[1:], delim, ans)

