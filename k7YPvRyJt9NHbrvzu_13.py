
def football(score):
    ans = 0
    for k2 in range(1 + score // 2):
        for k3 in range(1 + score // 3):
            for k6 in range(1 + score // 6):
                for k7 in range(1 + score // 7):
                    for k8 in range(1 + score // 8):
                        if 2 * k2 + 3 * k3 + 6 * k6 + 7 * k7 + 8 * k8 == score:
                            ans += 1
    return ans

