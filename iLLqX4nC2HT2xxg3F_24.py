
def deepest(L: list) -> int:
    counter, ans = 0, 0
    for char in str(L):
        if char == '[':
            counter += 1
            if counter > ans:
                ans = counter
        elif char == ']':
            counter -= 1
    return ans

