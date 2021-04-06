
def count_layers(rug):
    cnt = 1
    for i in range(1, len(rug) // 2 + 1):
        if rug[i] != rug[i-1]:
            cnt += 1
    return cnt

