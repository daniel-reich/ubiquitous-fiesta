
def largest_even(lst):
    ans = [x for x in lst if x % 2 == 0]
    i = 0
    if ans == []:
        return -1
    else:
        done = [ans[i]]
    while len(ans)>(i+1):
        if ans[i] < ans[i+1]:
            done = [ans[i+1]]
        ans = ans[1:]
        i += 1
    return done[0]

