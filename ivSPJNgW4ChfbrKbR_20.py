
def soroban(frame):
    for i in range(len(frame)):
        frame[i] = frame[i][::-1]
    ans = 0
    power = 1
    for elem in frame[0]:
        if elem == '|':
            # '5-bead' is active:
            ans += 5 * power
        power *= 10
    power = 1
    for col in range(len(frame[0])):
        cnt = 0
        idx = 3
        while idx < len(frame) and frame[idx][col] == 'O':
            cnt += 1
            idx += 1
        ans += cnt * power
        power *= 10
    return ans

