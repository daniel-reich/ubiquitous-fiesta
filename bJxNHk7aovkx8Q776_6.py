
def gold_distribution(gold):
    ans = [0, 0]
    while len(gold) > 0:
        for k in range(2):
            ans[k] += gold.pop() if gold[-1] > gold[0] else gold.pop(0)
    return ans

