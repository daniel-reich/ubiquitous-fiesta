
def greater_permutation(expr, nums):
    s = []
    for a in nums:
        for b in nums:
            for c in nums:
                if len(set([a, b, c])) == len(nums):
                    ex = expr
                    e = round(eval(expr), 2)
                    if ".0" in str(e):
                        e = int(str(e).replace(".0", ""))
                    ex = ex.replace("a", str(a))
                    ex = ex.replace("b", str(b))
                    ex = ex.replace("c", str(c))
                    add = [e, ex]
                    s.append(add)
    s = sorted(s, key=lambda x : x[0], reverse=True)
    return s[0][1] + " = " + str(s[0][0])

