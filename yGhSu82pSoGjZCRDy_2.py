
def seesaw(num):
    if num is None:
        return 'balanced'
    s = str(num)
    idx = len(s) // 2
    if len(s) % 2:
        left, right = s[:idx], s[idx+1:]
    else:
        left, right = s[:idx], s[idx:]
    if left < right:    return 'right'
    if left > right:    return 'left'
    return 'balanced'

