
def is_ascending(s):
    for k in range(1, len(s) // 2 + 1):
        if all(int(s[i + k:i + 2 * k]) - int(s[i: i + k]) == 1 for i in range(0, len(s) - k, k)):
            return True
    return False

