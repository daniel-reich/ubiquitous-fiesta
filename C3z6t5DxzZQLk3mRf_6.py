
target = [329.63, 246.94, 196, 146.83, 110, 82.41]
​
def tune(lst):
    ans = ['OK'] * 6
    for i in range(6):
        freq = lst[i]
        if freq == 0:
            ans[i] = ' - '
        elif abs(freq - target[i]) < 1e-4:
            ans[i] = 'OK'
        elif freq > target[i]:
            diff = 100 * (freq - target[i]) / target[i]
            if diff < .5:
                ans[i] = 'OK'
            elif diff < 2.5:
                ans[i] = '+<'
            else:
                ans[i] = '+<<'
        elif freq < target[i]:
            diff = 100 * (target[i] - freq) / target[i]
            if diff < .5:
                ans[i] = 'OK'
            elif diff < 2.5:
                ans[i] = '>+'
            else:
                ans[i] = '>>+'
    return ans

