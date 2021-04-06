
def block_player(a, b):
​
    if abs(a-b) == 2 or abs(a-b) == 6 or (a+b) == 8: return (a+b) // 2
​
    if abs(a-b) == 3:
        if max(a, b) in [3, 4, 5]: return max(a, b) + 3
        else: return min(a, b) - 3
​
    if abs(a - b) == 4:
        if max(a, b) == 4: return 4 + 4
        else: return 0
​
    if abs(a - b) == 1:
        if (a + b) % 3 ==0: return min(a, b) - 1
        else: return max(a, b) + 1
    if abs(a - b) == 1:
        if (a + b) % 3 ==0:
            return min(a, b) - 1
        else:
            return max(a, b) + 1

