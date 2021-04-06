
def jumping_frog(lng, stones):
    def jump(i, n):
        if i >= 0  and count[i] > n:
            count[i] = n
            jump(min(i+stones[i], lng), n+1)
            jump(i-stones[i], n+1)
                        
    stones.append(0)
    count = [lng*9] * (lng + 1)
    jump(0, 1)
    return "no chance :-(" if count[-1]>lng + 1 else count[-1]

