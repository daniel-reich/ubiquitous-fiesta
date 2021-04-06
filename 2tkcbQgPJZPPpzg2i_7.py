
digit_holes = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}
​
holes = {}
cur = 0
for i in range(1, 10**5):
    k = i
    cnt = 0
    while k > 0:
        cnt += digit_holes[k % 10]
        k //= 10
    cur += cnt
    holes[i] = cur
​
def sum_of_holes(N):
    return holes[N]

