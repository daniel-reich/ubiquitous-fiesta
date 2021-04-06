
def coins_div(lst):
    def next_step(i0, rest):
        for i, n in enumerate(lst[i0:], i0):
            if used[i]: continue
            if n <= rest:
                used[i] = True
                if n < rest:
                    yield from next_step(i+1, rest-n)
                else:
                    yield True
                used[i] = False
                
    if sum(lst) % 3: return False
    lst.sort(reverse=True)
    used = [False] * len(lst)
    for _1 in next_step(0, sum(lst) // 3):
        for _2 in next_step(1, sum(lst) // 3):
            return True
    return False

